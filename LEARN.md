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
[ "", "", "" ],
[ "", "", "" ],
[ "", "", "" ]
]
```
In the above lists, you'll see that it's three lists in one list and then in those lists there are three other strings. If we wanted to play tictactoe, it'd look something like this:

```
[
[ "x", "", "o" ],
[ "o", "x", "" ],
[ "", "", "x" ]
]
```
If we wanted to index the "x" in the top left, it'd be variableName[0][0].
This is because it is on the 0th row and 0th column. Rows are the:
```
[ "x", "", "o" ]
```
part & columns are the 
```
[ "x",
[ "o",
[ "",
```

Pretty simple right?

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

## Step Four, the game loop

```

    def Start(self):  # This is the main game loop function
        invalidAnswer = False
        controlFunctions = {"down": self.Down, "up": self.Up, "left": self.Left, "right": self.Right}
        while not self.dead and not invalidAnswer:

            answer = input("Up, down, left or right?").lower()
            if answer != "up" and answer != "down" and answer != "left" and answer != "right":
                print("That is not a valid answer!")
                invalidAnswer = True
            else:
                answerFunction = controlFunctions.get(answer.lower())
                answerFunction()
            print(DecryptBoard(self.boardList))
            print(f"Score: {self.score}")
            self.CheckDead()
        if invalidAnswer:
            self.Start()
        if self.dead:
            print(f"Game over! Final score: {self.score}")
```

### Syntax explanation
`controlFunctions = {"down": self.Down, "up": self.Up, "left": self.Left, "right": self.Right}` Is a [dictionary](https://www.w3schools.com/python/python_dictionaries.asp) and is [very fast](https://stackoverflow.com/q/40694470/15982771).

### Code explanation

The start function starts the game. We use `invalidAnswer` in case invalid input was inputted via the console. 
```
        while not self.dead and not invalidAnswer:
```
The above line ensures that the while loop doesn't run when the answer is invalid. Therefore,
```
        if invalidAnswer:
            self.Start()
```
If that's that case, the game gets restarted.

`controlFunctions` maps the string inputs to their function references. This makes it very fast because that function can be called from that reference. This cuts down a lot of code that would've been used in a bunch of if statements.
Although I could've used something else for:
```
if answer != "up" and answer != "down" and answer != "left" and answer != "right":
```
the above line checks for invalid input. If the input is valid, 
```
answerFunction = controlFunctions.get(answer.lower())
answerFunction()
```
The function is called. That function will control board movements. Ex: Player moves up, player moves right, etc.
Then the board is printed with `print(DecryptBoard(self.boardList))` (I'll get to that later).
& the score `print(f"Score: {self.score}")`. (Check dead does not work & I won't go over that cause the code is 2 years old)

## Step five, Movement
All of the keys were previously mapped to functions as described earlier. These functions are mapped to one singular function that moves the board.

```
    def Down(self):
        self.MoveTile((1, 0),
                      self.boardList, True)
        # Moves tile down (note: tuple order is (y,x)) (Also note: down is 1 and up is -1)

    def Right(self):
        self.MoveTile((0, 1), self.boardList, True)
        # Note that right is 1 and left is -1

    def Left(self):
        self.MoveTile((0, -1), self.boardList, True)

    def Up(self):
        self.MoveTile((-1, 0), self.boardList, True)
```
The `self.MoveTile` is that function.
```
    def MoveTile(self, direction, boardList,
                 mainBoard: bool):  # main board is to check if the board is the main board. This is to check the scoring
        movedItems = 0  # calculated to create new tiles
        if direction[0] > 0 or direction[1] > 0:
            for i in range(4):  # Push tiles down
                for y in range(boardY):
                    for x in range(boardX):
                        if boardList[y][x] != emptyChar:
                            try:
                                if boardList[y + direction[0]][x + direction[1]] == emptyChar:
                                    char = boardList[y][x]
                                    boardList[y][x] = emptyChar
                                    boardList[y + direction[0]][x + direction[1]] = char
                                    movedItems += 1
                            except IndexError:
                                pass
            for y in reversed(range(
                    boardY)):  # add tiles together (Note: The X and Y are reversed to calculate the merging properly based on the direction)
                for x in reversed(range(boardX)):
                    if boardList[y][x] != emptyChar:
                        try:
                            if boardList[y + direction[0]][x + direction[1]] == str(boardList[y][x]):
                                char = boardList[y][x]
                                boardList[y][x] = emptyChar
                                boardList[y + direction[0]][x + direction[1]] = str(
                                    int(char) * 2)  # multiplies the tile by 2 when merging
                                movedItems += 1
                                if mainBoard:
                                    self.score += int(char) * 2

                        except IndexError:
                            pass
            for i in range(4):  # Push tiles down again
                for y in range(boardY):
                    for x in range(boardX):
                        if boardList[y][x] != emptyChar:
                            try:  # try catch function to check if the index goes out of the board
                                if boardList[y + direction[0]][x + direction[1]] == emptyChar:
                                    char = boardList[y][x]
                                    boardList[y][x] = emptyChar
                                    boardList[y + direction[0]][x + direction[1]] = char
                                    movedItems += 1
                            except IndexError:
                                pass
        # left and up directions
        elif direction[0] < 0 or direction[1] < 0:
            for i in range(boardX + boardY):  # calculates pushing the tiles multiple times
                for y in range(boardY):
                    for x in range(boardX):
                        if boardList[y][x] != emptyChar:  # checks if the current tile is empty
                            if (y != 0 and direction[0] != 0) or (x != 0 and direction[1] != 0):
                                # special case where tiles could move off of the board because we are using negative list indexes
                                if boardList[y + direction[0]][x + direction[1]] == emptyChar:
                                    char = boardList[y][x]
                                    boardList[y][x] = emptyChar
                                    boardList[y + direction[0]][x + direction[1]] = char
                                    movedItems += 1
            for y in range(boardY):  # adds the tiles together
                for x in range(boardX):
                    if boardList[y][x] != emptyChar:
                        if boardList[y + direction[0]][x + direction[1]] == boardList[y][x]:
                            if (y != 0 and direction[0] != 0) or (x != 0 and direction[1] != 0):
                                char = boardList[y][x]
                                boardList[y][x] = emptyChar
                                boardList[y + direction[0]][x + direction[1]] = str(int(char) * 2)
                                movedItems += 1
                                if mainBoard:
                                    self.score += int(char) * 2
            for i in range(boardX + boardY):  # calculates pushing the tiles again
                for y in range(boardY):
                    for x in range(boardX):
                        if boardList[y][x] != emptyChar:  # checks if the current tile is empty
                            if (y != 0 and direction[0] != 0) or (x != 0 and direction[1] != 0):
                                # special case where tiles could move off of the board because we are using negative list indexes
                                if boardList[y + direction[0]][x + direction[1]] == emptyChar:
                                    char = boardList[y][x]
                                    boardList[y][x] = emptyChar
                                    boardList[y + direction[0]][x + direction[1]] = char
                                    movedItems += 1
```
This is the most confusing function out of them all. Do note that I did make this code 2 years ago...

`# main board is to check if the board is the main board. This is to check the scoring` was a very confusing comment

### Code explanation
It's a lot of boilerplate. But we can get through it. Let's start small.
```
        if direction[0] > 0 or direction[1] > 0:
```
Checks the direction for if it's right or down (-1 is up because of lists).
