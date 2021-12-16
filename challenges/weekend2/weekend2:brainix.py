'''Redis DEVcember weekend 2.

When I ran this Python script, I got the following output:

RedisSet cardinality: 5000
BloomFilter count: 4984
HyperLogLog count: 4950

RedisSet known UUIDs: 5000 hits, 0 misses, 18 ms
RedisSet unknown UUIDs: 0 hits, 5000 misses, 15 ms
BloomFilter known UUIDs: 5000 hits, 0 misses, 327 ms
BloomFilter unknown UUIDs: 55 hits, 4945 misses, 327 ms
HyperLogLog known UUIDs: 5000 hits, 0 misses, 128 ms
HyperLogLog unknown UUIDs: 877 hits, 4123 misses, 128 ms
'''


import uuid

from redis import Redis
from pottery import BloomFilter
from pottery import ContextTimer
from pottery import HyperLogLog
from pottery import RedisSet


# I'm running stock Redis 6.2.6 locally, without the Bloom Filter module
# installed.
redis = Redis()
REDISSET_KEY, BLOOMFILTER_KEY, HYPERLOGLOG_KEY = 'uuids:set', 'uuids:bloom', 'uuids:hll'
redis.delete(REDISSET_KEY, BLOOMFILTER_KEY, HYPERLOGLOG_KEY)

# 1. Create a collection of unique elements.
NUM_ELEMENTS = 5_000
known_uuids, unknown_uuids = [], []
for list_ in (known_uuids, unknown_uuids):
    for _ in range(NUM_ELEMENTS):
        uuid_ = str(uuid.uuid4())
        list_.append(uuid_)

# 2. Create and populate a set with your unique elements.  I've authored a
# library called Pottery (https://github.com/brainix/pottery) for accessing
# Redis more Pythonically.  Use Pottery's RedisSet container for convenience:
redis_set = RedisSet(known_uuids, redis=redis, key=REDISSET_KEY)

# 3. Create and populate a Bloom filter with your unique elements.  Pottery's
# BloomFilter is a pure Python implementation.  Its advantages are:
#   - It exposes an easy to use, Python set like API
#   - It works on a stock Redis instance without the Bloom Filter module
#     installed
#
# RedisBloom offers these advantages:
#   - It's implemented in C and runs on the Redis server, so it's likely far
#     more performant (I've never used it or benchmarked it against Pottery's
#     BloomFilter)
#   - It offers more data types beyond Pottery's simple Bloom filter (including
#     a cuckoo filter, a count-min sketch, and a top-k)
#
# Here, let's use Pottery's BloomFilter for ease:
bloom_filter = BloomFilter(
    known_uuids,
    redis=redis,
    key=BLOOMFILTER_KEY,
    num_elements=NUM_ELEMENTS,
    false_positives=0.01,
)

# 4. Create and populate a HyperLogLog with your unique elements.  Use Pottery's
# HyperLogLog for code ergonomics:
hll = HyperLogLog(known_uuids, redis=redis, key=HYPERLOGLOG_KEY)

# 5. Count the number of unique members within each data structure.  Python's
# built-in len() function works on Pottery's RedisSets, BloomFilters, and
# HyperLogLogs!  :-)
print()
print('RedisSet cardinality:', len(redis_set))
print('BloomFilter count:', len(bloom_filter))
print('HyperLogLog count:', len(hll))

# 6. Bonus time!  Check the UUIDs against the three data structures to see just
# how probabilistic they really are!  Let's use Pottery's ContextTimer to
# handily measure execution time.  We can use Python's "in" keyword to do
# membership testing against Pottery's RedisSets, BloomFilters, and
# HyperLogLogs.  Additionally, we can use .contains_many() to do more efficient
# membership testing for multiple elements.  Let's use .contains_many().
print()
for list_, label in ((known_uuids, 'known'), (unknown_uuids, 'unknown')):
    with ContextTimer() as timer:
        redis_set_hits = sum(redis_set.contains_many(*list_))
    redis_set_misses = len(list_) - redis_set_hits
    print(f'RedisSet {label} UUIDs: {redis_set_hits} hits, {redis_set_misses} misses, {timer.elapsed()} ms')

for list_, label in ((known_uuids, 'known'), (unknown_uuids, 'unknown')):
    with ContextTimer() as timer:
        bloom_filter_hits = sum(bloom_filter.contains_many(*list_))
    bloom_filter_misses = len(list_) - bloom_filter_hits
    print(f'BloomFilter {label} UUIDs: {bloom_filter_hits} hits, {bloom_filter_misses} misses, {timer.elapsed()} ms')

for list_, label in ((known_uuids, 'known'), (unknown_uuids, 'unknown')):
    with ContextTimer() as timer:
        hll_hits = sum(hll.contains_many(*list_))
    hll_misses = len(list_) - hll_hits
    print(f'HyperLogLog {label} UUIDs: {hll_hits} hits, {hll_misses} misses, {timer.elapsed()} ms')

# Clean up after ourselves.
redis.delete(REDISSET_KEY, BLOOMFILTER_KEY, HYPERLOGLOG_KEY)
