# DEVcember Weekend 3 Challenge

In this challenge, you'll get to use Redis OM for Node.js.  You'll want to have a Redis Cloud database setup with the RediSearch module installed before proceeding.  Alternatively, if you're using Docker, we've provided a Docker Compose file that will start Redis + RediSearch in a container for you.

## Get Started

First, clone this repository:

```bash
$ git clone https://github.com/redis-developer/devcember.git
$ cd challenges/weekend3

Then, install the dependencies:

```bash
$ npm install
```

If you want to run Redis with RediSearch locally, start the Docker container in the background:

```bash
$ docker-compose up -d
```

If you're using Redis in the cloud, you'll need to pass a Redis URL to `client.open` in both `query_animals.js` and `load_animals.js`.  See the [Redis OM Node.js documentation](https://github.com/redis-developer/devcember.git) for information.


Load the data into Redis (check out the code in `load_animals.js` to see how this works):

```bash
$ npm run load
```

Run the sample query (check out the code in `query_animals.js`), which finds all male dogs that are more than 3 years old:

```bash
$ npm run query
```

## Write Some Search Queries

This weekend's challenge is open ended... using the animal data provided, and the Redis OM for Node.js query API ([examples here](https://github.com/redis/redis-om-node#-using-redisearch))... modify the query at line 10 in `query_animals.js` to perform other queries of your own design.  

Be sure to try out the [full-text search](https://github.com/redis/redis-om-node#full-text-search) capabilities on the `description` field.

Show us what you make! Create a copy of `query_animals.js` and call it `query_animals:<YOUR GITHUB USERNAME>.js`.  Submit a pull request to the repository and your effortd will be added and reviewed befor the end of Devcember on December 24th 2021.

## Weekend 3 Challenge Resources

You may find the following resources helpful:

* Day 01 - [Get Started with Redis in the Cloud](https://youtu.be/jf-lwkWUQHg)
* Day 02 - [Up and Running with RedisInsight](https://www.youtube.com/watch?v=S-CXWP50ewM)
* Day 12 - [Introducing Redis OM for Node.js](https://www.youtube.com/watch?v=y0Sx_5Csld8) 
* [Redis OM for Node.js](https://github.com/redis/redis-om-node)