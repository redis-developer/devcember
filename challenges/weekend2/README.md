Try Redis-Om for Python https://github.com/redis/redis-om-python

# DEVcember Weekend 2 Challenge

Let's practice our skills with the Redis Sets, Bloom Filter, and Hyperlolglog data types! You'll want to have your RedisInsight instance up and running with your Redis Cloud database connected in order to answer the challenge questions in this document. 

With a free Redis instance you'll have the RedisBloom module available at the point of database creation in the Redis Cloud UI. Make sure to enable the RedisBloom module before proceeding with the challenge.

Clone this repository, create a branch named `weekend2:<YOUR GITHUB USERNAME>` and rename the `weekend2.py` file to `weekend2:<YOUR GITHUB USERNAME>.py`. Submit a pull request to the repository and your efforts will be added and reviewed by December 13th, 12:00pm PST.  Remember that there are many different solutions to a single problem, so don't be afraid to be as creative as you'd like. 

### Weekend 2 Challenge Resources:
- [Day 04 - Lets try out Redis OM for Python](https://youtu.be/gi6jugJsKS4)
- [Day 05 - The Scoop on Big O Notation](https://youtu.be/xSuZjetOhgs)
- [Day 06 - Get! Set! Go!](https://youtu.be/e1wD52EAiQw)
- [Day 07 - Have I Seen You Before? Introducing Bloom Filters](https://youtu.be/qgJRoWBmEoQ)
- [Day 08 - You Can (Mostly) Count on Hyperloglog!](https://youtu.be/pUpSnaqpcks)
- [Redis Set Commands](https://redis.io/commands#set)
- [Redis Set Explainer](https://youtu.be/PKdCppSNTGQ)
- [Redis Hyperloglog Explainer](https://www.youtube.com/watch?v=MunL8nnwscQ)
- [Redis Bloom Filter Explainer](https://youtu.be/Z9_wrhdbSC4)
- [Redis Bloom Filter Documentation](https://oss.redis.com/redisbloom/Bloom_Commands/)

### Weekend 2 python code challenge
In this week's challenge, you'll be working within the `weekend2.py` file.  Some initial code has been provided to get you started. You'll want to connect a Redis instance via environment variables. Note that your Redis instance *MUST* have the RedisBloom module in order to create and use Bloom Filters.

1.  Within the python code you'll se a section creating random UUIDs. For this code challenge we'll use these UUIDs to populate the three different data structures. Feel free to use any other methodology you'd like.

2. `weekend2.py` has a single command illustrating how to add a single member to the Set data structure. Implement code to add multiple members to the Set. You can use the provided UUID list or implement your own methods.

3. `weekend2.py` also has a single command illustrating how to add a single member to the Redis Bloom data structure. Implement code to add multiple members to the Bloom Filter.  You can use the provided UUID list or implement your own methods.

4. Lastly, `weekend2.py` has a single command illustrating how to add a single member to the Hyperloglog data structure. Implement code to add multiple members to the Hyperloglog. You can use the provided UUID list or implement your own methods.

5. We'll want to see how many members were successfully entered into each data structure. Find the necessary commands for each data structure to return the unique member count.

6. Bonus time! Now's your chance to implement code to check just how probabilistic these data structures really are. Iterate through the original source list of your members and check if they exist in your data structures. Keep a running tally of hits and misses. You should expect sets to be completely full of hits and the Bloom Filter and Hyperloglog slightly less than perfect, as is designed.  You can also add timing for each data structure check to see the difference in time between all three data structures. Share your findings on the [#devcember discord channel](https://discord.gg/ZKws9zy9)!