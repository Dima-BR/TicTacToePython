# 🎮 Tic Tac Toe Game in Python

This is a simple implementation of the Tic Tac Toe game in Python. The game allows a player to play against the computer.

## 📋 Table of Contents

1. [Board Initialization](#board-initialization)
2. [Constants](#constants)
3. [Functions](#functions)
    - [draw_board](#draw_board)
    - [convert_location_to_position](#convert_location_to_position)
    - [free_locations](#free_locations)
    - [player_move](#player_move)
    - [computer_move](#computer_move)
    - [is_winner](#is_winner)
4. [Main Function](#main-function)
5. [Entry Point](#entry-point)

## 🛠️ Board Initialization

The game board is initialized as a list of lists, where each sublist represents a row on the board. Each cell in the board is initially filled with a number representing the cell location.

```python
board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

## 🔤 Constants

Two constants `X` and `O` are defined to represent the two players.

```python
X = 'X'
O = 'O'
```

## ⚙️ Functions

### 🖼️ draw_board

This function prints the current state of the board.

```python
def draw_board(board):
    print(f"\t{board[0][0]}\t|\t{board[0][1]}\t|\t{board[0][2]}\t")
    print('-' * 25)
    print(f"\t{board[1][0]}\t|\t{board[1][1]}\t|\t{board[1][2]}\t")
    print('-' * 25)
    print(f"\t{board[2][0]}\t|\t{board[2][1]}\t|\t{board[2][2]}\t")
```

### 🔄 convert_location_to_position

This function converts a location number (1-9) to board coordinates (row, col).

```python
def convert_location_to_position(location):
    row = (location - 1) // 3
    col = (location - 1) % 3
    return row, col
```

### 🆓 free_locations

This function returns a list of free locations on the board.

```python
def free_locations(board):
    free = []
    for raw in board:
        for col in raw:
            if isinstance(col, int):
                free.append(col)
    return free
```

### 👤 player_move

This function handles the player's move.

```python
def player_move():
    free = free_locations(board)
    while True:
        location = input(f"List of free locations {free}\nEnter the location of your move: ")
        try:
            location = int(location)
        except ValueError:
            print(f"Location must be a valid integer.\n Please try again")
            continue
        if location not in free:
            print(f"Please chose available location.")
            continue
        break

    row, col = convert_location_to_position(location)
    board[row][col] = player
    draw_board(board=board)
```

### 🤖 computer_move

This function handles the computer's move using a random choice from the list of free locations.

```python
def computer_move():
    free = free_locations(board)
    location = random.choice(free)
    row, col = convert_location_to_position(location)
    board[row][col] = computer
    draw_board(board=board)
```

### 🏆 is_winner

This function checks if there is a winner.

```python
def is_winner(board):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    if [player, player, player] in win_conditions:
        return player
    elif [computer, computer, computer] in win_conditions:
        return computer
    return False
```

## 🏁 Main Function

The `main` function initializes the game and handles the game loop.

```python
def main():
    draw_board(board)

    if is_first:
        player_move()

    while not is_winner(board) and free_locations(board):
        computer_move()
        if not is_winner(board) and free_locations(board):
            player_move()

    winner = is_winner(board)
    if winner == X or winner == O:
        print(f"Player with {winner} is the winner!")
    else:
        print("It's a draw!")
```

## 🔚 Entry Point

The script starts here, asking the player to choose their symbol and whether they want to start first.

```python
if __name__ == "__main__":
    while True:
        player = input("X or O? ").upper()
        if player not in [X, O]:
            print("Please enter a valid input ... try again")
            continue
        if player == X:
            computer = O
        else:
            computer = X

        print(f"Computer will play with {computer}")
        break

    while True:
        is_first = input("Do you want to start first? [Y/n]").upper()
        if is_first in ["Y", "YES", "YEAH"]:
            is_first = True
            print("Player will start first")
        elif is_first in ["N", "NO", "NAH"]:
            is_first = False
            print("Computer will start first")
        else:
            print("Please enter a valid input ... try again")
            continue
        break

    main()
