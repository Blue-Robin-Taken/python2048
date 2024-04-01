# How to make 2048 in Python!

## Prerequisites

Basic python knowledge.
- [Variables](https://www.w3schools.com/python/python_variables.asp)
- [Casting/Type Changing](https://www.w3schools.com/python/python_variables.asp)
- [Imports](https://www.w3schools.com/python/python_modules.asp)
- [Functions](https://www.w3schools.com/python/python_functions.asp)
- [Classes](https://www.w3schools.com/python/python_classes.asp)

## Step One, imports

```
# --- imports ---
import random
import os
import copy
```
We'll be using the above imports later.

## Step Two, Create the basic class

```
class TwentyFortyEight:
    def __init__(self, consoleOn):  # consoleOn is a bool that allows printing or not printing
        # --- Starting variables ---
        self.score = 0
        self.dead = False
```

### Syntax explanation

The `__init__` is called when the class is instanced. To find out more about that, see [here](https://stackoverflow.com/a/625098/15982771)
The `self` is a reference back to the class. We can change the properties of the class via [`self`](https://www.geeksforgeeks.org/self-in-python-class/)

### Code explanation

We're just saving two properties of the game into the class. The score and if the game is dead (death not yet implemented).

## Step Three, Generating the board

```
        # --- Generate boardList ---
        rows = []
        for y in range(boardY):
            rows.append("⬜")
        columns = []
        for x in range(boardX):
            columns.append(rows.copy())
        self.boardList = columns
        for i in range(2):  # Create two twos in the board
            randomNumber = random.randint(1, 2)
            if randomNumber == 1:
                randomEmptyTile = GetEmptyTiles(self.boardList)[random.randrange(0, len(GetEmptyTiles(self.boardList)))]
                self.boardList[randomEmptyTile[0]][randomEmptyTile[1]] = "2"
            elif randomNumber == 2:
                randomEmptyTile = GetEmptyTiles(self.boardList)[random.randrange(0, len(GetEmptyTiles(self.boardList)))]
                self.boardList[randomEmptyTile[0]][randomEmptyTile[1]] = "4"
```

### Syntax explanation

`rows=[]` creates a new [empty list](https://www.w3schools.com/python/python_lists.asp).
`for i in range(2):` is a basic [for loop](https://www.w3schools.com/python/python_for_loops.asp).
`.append("⬜")` is to add "⬜" to the list.
`rows.copy()` creates a "copy" of that list so that we aren't editing the original list (if you don't make a copy, you create a [reference](https://stackoverflow.com/q/2612802/15982771)).

### Code explanation

#### How the lists work

To create the board we need to make a 2d list. That's just multiple lists inside a list. For example:
```
[
[ [], [], [] ],
[ [], [], [] ],
[ [], [], [] ]
]
```
In the above lists, you'll see that it's three lists in one list and then in those lists there are three other lists. If we wanted to play tictactoe, it'd look something like this:

```
[
[ ["x"], [], ["o"] ],
[ ["o"], ["x"], [] ],
[ [], [], ["x"] ]
]
```
We'll call the lists inside the big list columns. The lists in those lists are rows.

#### Actual code

Now, in the actual code, `boardY` was a var set previously (global var, ik, bad). 
```
        for y in range(boardY):
            rows.append("⬜")
```
This part just fills the rows with the background character.

```
        columns = []
        for x in range(boardX):
            columns.append(rows.copy())
```
In the above, we're duping the rows multiple times & adding it to cols. It's a little confusing though because I named the vars `boardX` and `boardY` even though they're flipped.
