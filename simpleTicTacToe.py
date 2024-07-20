# Tic Tac Toe
# Create board as List number
import random
board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

X = 'X'
O = 'O'
# draw board using function
def draw_board(board):
    print(f"\t{board[0][0]}\t|\t{board[0][1]}\t|\t{board[0][2]}\t")
    print('-' * 25)
    print(f"\t{board[1][0]}\t|\t{board[1][1]}\t|\t{board[1][2]}\t")
    print('-' * 25)
    print(f"\t{board[2][0]}\t|\t{board[2][1]}\t|\t{board[2][2]}\t")


def convert_location_to_position(location):
    row = (location - 1) // 3
    col = (location - 1) % 3
    return row, col

def free_locations(board):
    free = []
    for raw in board:
        # print("row", raw)
        for col in raw:
            # print("col", col)
            # if col in range(1, 10):
            #     free.append(col)
            if isinstance(col, int):
                free.append(col)
    return free

def player_move():  # function are first class citizen, and also is an object
    free = free_locations(board)
    # print(f"free {free}")
    while True:
        location = input(f"List of free locations {free}\nEnter the location of your move: ")
        try:
            location = int(location)
            print(f"location {location}")
        except ValueError as e:
            print(f"Location must be a valid integer.\n Please try again")
            continue
        if location not in free:
            print(f"Please chose available location.")
            continue

        break

    raw, col = convert_location_to_position(location)
    print(convert_location_to_position(location))
    board[raw][col] = player
    print(f"player = {player}")
    draw_board(board=board)

def computer_move():  # function are first class citizen, and also is an object
    free = free_locations(board)
    location = random.choice(free) # minimax()
    print(f"location {location}")
    raw, col = convert_location_to_position(location)
    board[raw][col] = computer
    draw_board(board=board)

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

if __name__ == "__main__":  # validation
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
