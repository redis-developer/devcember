import os
import redis
import uuid

# You can use your free cloud instance of Redis for these challenges, or a local instance 
# Make sure you have the Bloom Filter module included with the Redis instance
r = redis.Redis(
    host=os.getenv('REDIS_HOST'),
    port=os.getenv('REDIS_PORT'), 
    password=os.getenv('REDIS_PASS'))

# 1. Create a collection of unique elements.
uuid_list = []
for x in range(5000):
    uuid_list.append(str(uuid.uuid4()))

# Start a pipeline for your commands
pipe = r.pipeline()

# 2. Create and populate a Set with your unique elements
# Try entering a larger amount, perhaps in the thousands.
pipe.sadd('unique_set', uuid_list[0])

# 3. Create and populate a Bloom Filter with your unique elements
# Try entering a larger amount, perhaps in the thousands.
pipe.execute_command('bf.add', 'unique_bloom_filter', uuid_list[0])


# 4. Create and populate a Hyperloglog with your unique elements
# Try entering a larger amount, perhaps in the thousands.
pipe.pfadd('unique_hyperlolog', uuid_list[0])

# Execute the pipeline of commands
pipe.execute()

# 5. Determine the amount of unique members within each data structure
set_count = 0 # Enter code here to determine the cardinality of the set
bf_count = 0 # Enter code here to determine the amount of members in the Bloom Filter
hll_count = 0 # Enter code here to determine the amount of members in the Hyperloglog

print(f'Set cardinality: {set_count}')
print(f'Bloom-filter count: {bf_count}')
print(f'Hyperloglog count: {hll_count}')    


# 6. Bonus time! Check the uuid_list against the three data structure to see just how probabilistic they really are!
