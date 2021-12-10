# DEVcember Weekend 1 Challenge

Let's practice our skills with the Redis List data type! You'll want to have your RedisInsight instance up and running with your Redis Cloud database connected in order to answer the challenge questions in this document.  

Clone this repository, create a branch named `weekend1:<YOUR GITHUB USERNAME>` and rename this README.md to `weekend1:<YOUR GITHUB USERNAME>.md`. Submit a pull request to the repository and your efforts will be added and reviewed by December 6th, 12:00pm PST.  Remember that there are many different solutions to a single problem, so don't be afraid to be as creative as you'd like. 

### Weekend 1 Challenge Resources:
- [Day 01 - Getting Started with Redis Cloud](https://www.youtube.com/watch?v=jf-lwkWUQHg)
- [Day 02 - Up and Running with RedisInsight](https://www.youtube.com/watch?v=jf-lwkWUQHg)
- [Day 03 - The Redis List goes on and on!](https://www.youtube.com/watch?v=OjoAmWOPk64)
- [Redis List Commands](https://redis.io/commands#list)
- [Redis List Explainer](https://www.youtube.com/watch?v=PB5SeOkkxQc)


###  1. Creating a list
What command or commands are required to create the following List named `months` in Redis?

```javascript
["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
```

I've authored a library called [Pottery](https://github.com/brainix/pottery) for accessing Redis more Pythonically. Install it by creating/activating a virtual environment and using `pip3` like so:

```zsh
% ~/.pyenv/versions/3.10.1/bin/python3 -m venv venv   
% source venv/bin/activate
(venv) % pip3 install pottery
```

Then use Pottery's [`RedisList`](https://github.com/brainix/pottery#lists) container to create the list like so:

```python
>>> from pottery import RedisList
>>> from redis import Redis
>>> redis = Redis()
>>> months = RedisList(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], redis=redis, key='months')
>>> months
RedisList['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
```




### 2. Accessing elements in a list
 What commands would you use to access the 3rd and 5th elements in the `months` list?

```python
>>> months[2]
'March'
>>> months[4]
'May'
```




### 3. In your own words
What are some possible use cases not already covered for a Stack data structure in Redis? 

One use case for a Redis-backed stack is to maintain an undo history. Whenever a user performs an undoable action, append the action to the left of the stack. Then whenever the user clicks undo, pop the action from the left of the stack and undo it.




### 4. In your own words
What are some possible use cases not already covered for a Queue data structure in Redis? 

One use case for a Redis-backed queue is to maintain a printer spooler. Whenever a new document comes in to be printed, add it to the rear of the queue. Whenever the printer finishes printing a document, pop the next document off of the front of the queue.




## Bonus: Circular List Data Structure

Suze, Simon, Justin, Guy, Brian, and Steve are all designing an online boardgame and want to keep track of the current player's turn using a circular list. Whoever is at index 0 of the circular list is the current player who should play their turn. They begin by making themselves players in a test game. 

### 1. Creating a Circular List
How would you initialize a Circular List named `game:prototype` with the players Suze, Simon, Justin, Guy, Brian, and Steve?

```python
>>> from pottery import RedisDeque
>>> from redis import Redis
>>> redis = Redis()
>>> players = RedisDeque(['Suze', 'Simon', 'Justin', 'Guy', 'Brian', 'Steve'], redis=redis, key='game:prototype')
>>> players
RedisDeque(['Suze', 'Simon', 'Justin', 'Guy', 'Brian', 'Steve'])
```




### 2. Iterating a Circular List
Assume Suze took her turn and now it is Simon's turn to play. How would you reflect this state in the `game:prototype` list?

```python
>>> players.rotate(-1)
>>> players
RedisDeque(['Simon', 'Justin', 'Guy', 'Brian', 'Steve', 'Suze'])
```




### 3. Removing an element from a Circular List
Unfortunately, Simon had to leave the game to help someone on the [Redis Discord Server](https://discord.gg/redis). How would we go about removing Simon from the `game:prototype` list and ensure that Justin plays next?

```python
>>> players.popleft()
'Simon'
>>> players
RedisDeque(['Justin', 'Guy', 'Brian', 'Steve', 'Suze'])
```




### 4. Inserting a new element into a Circular List
A new player has entered the game! How would we go about entering Kyle into the `game:prototype` list? (Assume Justin has just played his turn so Guy, Brian, and Steve still have yet to play)

```python
>>> players.rotate(-1)
>>> players.append('Kyle')
>>> players
RedisDeque(['Guy', 'Brian', 'Steve', 'Suze', 'Justin', 'Kyle'])
```



