# DEVcember Weekend 1 Challenge

Lets practice our skills with the Redis List data type! You'll want to have your Redis Insight instance up and running with your Redis Cloud database connected in order to answer the challenge questions in this document.  

Clone this repository, create a branch named `weekend1:<YOUR GITHUB USERNAME>` and rename this README.md to `weekend1:<YOUR GITHUB USERNAME>.md`. Submit a pull request to the repository and your efforts will be added and reviewed by [INSERT REASONABLE DEADLINE HERE].  Remember that there are many different solutions to a single problem, so don't be afraid to be as creative as you'd like. 

### Weekend 1 Challenge Resources:
- [Day 01](https://www.youtube.com/watch?v=jf-lwkWUQHg)
- [Day 02](https://www.youtube.com/watch?v=jf-lwkWUQHg)
- [Day 03](https://www.youtube.com/watch?v=OjoAmWOPk64)
- [Redis List Commands](https://redis.io/commands#list)
- [Redis List Explainer](https://www.youtube.com/watch?v=PB5SeOkkxQc)


###  1. Creating a list
What command or commands are required to create the following List named `months` in Redis?

```javascript
["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
```

[Enter your command or commands here]


### 2. Accessing elements in a list
What commands would you use to access the 3rd and 5th elements in the `months` list?

[Enter your command or commands here]


### 3. What are some possible use cases not already covered for a Stack data structure in Redis? 

[Enter your answer here]


### 4. What are some possible use cases not already covered for a Queue data structure in Redis? 

[Enter your answer here]



## Bonus: Circular List Data Structure

Suze, Simon, Justin, Guy, Brian, and Steve are all designing an online boardgame and want to keep track of the current player's turn using a circular list. Whoever is at index 0 of the circular list is the current player who should play their turn. They begin by making themselves players in a test game. 

### How would you initialize a Circular List named `game:prototype` with the players Suze, Simon, Justin, Guy, Brian, and Steve?

[Enter your command or commands here]

### Assume Suze took her turn and now it is Simon's turn to play. How would you reflect this state in the `game:prototype` list?

[Enter your command or commands here]

### Unfortunately, Simon had to leave the game to help someone on the [Redis Discord Server](https://discord.gg/redis). How would we go about removing Simon from the `game:prototype` list and ensure that Justin plays next?

[Enter your command or commands here]

### A new player has entered the game! How would we go about entering Kyle into the `game:prototype` list? (Assume Justin has just played his turn so Guy, Brian, and Steve still have yet to play)

[Enter your command or commands here]

