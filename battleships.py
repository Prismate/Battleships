import time
import os
# import replit

SHIP_TYPE = [4, 3, 2, 1]
PLAYER = ['PLAYER_1', 'PLAYER_2']
LETTERS_TO_NUMBERS = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4
}

player_1 = [
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."]
    ]
player_2 = [
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."]
    ]
player_1_guess = [
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."]
    ]
player_2_guess = [
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."]
    ]

class bcolors:
    HEADER_1 = '\033[93m'
    HEADER_2 = '\033[95m'
    FAIL = '\033[91m'
    WINNER = '\033[92m'
    XX = '\033[94m'
    OO = '\033[95m'
    END = "\033[0m"

def get_empty_board():
    board = [
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."]
    ]
    return board

def display_board(board):
    print("  1 2 3 4 5")
    print(f"A {board[0][0]} {board[0][1]} {board[0][2]} {board[0][3]} {board[0][4]}")
    print(f"B {board[1][0]} {board[1][1]} {board[1][2]} {board[1][3]} {board[1][4]}")
    print(f"C {board[2][0]} {board[2][1]} {board[2][2]} {board[2][3]} {board[2][4]}")
    print(f"D {board[3][0]} {board[3][1]} {board[3][2]} {board[3][3]} {board[3][4]}")
    print(f"E {board[4][0]} {board[4][1]} {board[4][2]} {board[4][3]} {board[4][4]}")

def user_input(place_ship):
    if place_ship == True:
        while True:
            try:
                position = input("Enter position of ship (H or V): ").upper().strip()
                if position == "H" or position == "V":
                    break
                else:
                    raise ValueError
            except:
                print("Enter a valid position!")
        while True:
            try:
                row = input("Enter a row of ship (A-E): ").upper().strip()
                if row in "ABCDE":
                    row = LETTERS_TO_NUMBERS[row]
                    break
                else:
                    raise ValueError
            except:
                print("Enter a valid row!")
        while True:
            try:
                column = input("Enter a column of ship (1-5): ").strip()
                if column in "12345":
                    column = int(column) - 1
                    break
                else:
                    raise ValueError
            except:
                print("Enter a valid column!")

        return position, row, column
    else:
        while True:
            try:
                row = input("Enter a row of ship (A-E): ").upper().strip()
                if row in "ABCDE":
                    row = LETTERS_TO_NUMBERS[row]
                    break
                else:
                    raise ValueError
            except:
                print("Enter a valid row!")
        while True:
            try:
                column = input("Enter a column of ship (1-5): ").strip()
                if column in "12345":
                    column = int(column) - 1
                    break
                else:
                    raise ValueError
            except:
                print("Enter a valid column!")

        return row, column

def place_ships(board):
    for current_player in PLAYER:
        if current_player == 'PLAYER_1':
            if board == player_1:
                print(bcolors.HEADER_1 + f"\n\n\n\n\n\n\n{current_player} turn!" + bcolors.END)
                display_board(board)
                for ship_len in SHIP_TYPE:
                    while True:
                        # if board == player_1:
                        place_ship = True
                        # display_board(board)
                        print(f"\nEnter the position for a ship with len {ship_len}")
                        position, row, column = user_input(place_ship)
                        if valid_placement(ship_len, row, column, position) == True:
                            if ship_overwrites(board, row, column, position, ship_len) == True:
                                if available_space(board, row, column, position, ship_len) == True:
                                    if position == "H":
                                        for i in range(column, column + ship_len):
                                            board[row][i] = "X"
                                    else:
                                        for i in range(row, row + ship_len):
                                            board[i][column] = "X"
                                    print("\n")
                                    display_board(player_1)
                                    break
        else:
            if board == player_2:
                print(bcolors.HEADER_1 + f"\n{current_player} turn!" + bcolors.END)
                display_board(board)
                for ship_len in SHIP_TYPE:
                    while True:
                        # if board == player_1:
                        place_ship = True
                        # display_board(board)
                        print(f"\nEnter the position for a ship with len {ship_len}")
                        position, row, column = user_input(place_ship)
                        if valid_placement(ship_len, row, column, position) == True:
                            if ship_overwrites(board, row, column, position, ship_len) == True:
                                if available_space(board, row, column, position, ship_len) == True:
                                    if position == "H":
                                        for i in range(column, column + ship_len):
                                            board[row][i] = "X"
                                    else:
                                        for i in range(row, row + ship_len):
                                            board[i][column] = "X"
                                    print("\n")
                                    display_board(player_2)
                                    break

def valid_placement(ship_len, row, column, position):
    if position == "H":
        if column + ship_len <= 5:
            return True
    elif position == "V":
        if row + ship_len <= 5:
            return True
    print("Your ship is too long!")
    return False

def ship_overwrites(board, row, column, position, ship_len):
    if position == "H":
        for i in range(column, column + ship_len):
            if board[row][i] == "X":
                print("This position is already taken! Enter a valid coordinates!")
                return False
    elif position == "V":
        for i in range(row, row + ship_len):
            if board[i][column] == "X":
                print("This position is already taken! Enter a valid coordinates!")
                return False
    return True

def available_space(board, row, column, position, ship_len):
    space = []
    if position == "H":
        if row > 0:
            count = 0
            for i in range(column, column + ship_len):
                space.append(board[row-1][column+count])
                count += 1
        count = 0
        for i in range(column, column + ship_len):
            space.append(board[row][column + count])
            count += 1
        if row + ship_len < 4:
            count = 0
            for i in range(column, column + ship_len):
                space.append(board[row + 1][column + count])
                count += 1
        if column != 0:
            space.append(board[row][column - 1])
        if column + ship_len < 5:
            space.append(board[row][column + ship_len])
    elif position == "V":
        if column > 0:
            count = 0
            for i in range(row, row + ship_len):
                space.append(board[row + count][column - 1])
                count += 1
        count = 0
        for i in range(row, row + ship_len):
            space.append(board[row + count][column])
            count += 1
        if column + ship_len < 4:
            count = 0
            for i in range(row, row + ship_len):
                space.append(board[row + count][column + 1])
                count += 1
        if row != 0:
            space.append(board[row - 1][column])
        if row + ship_len < 5:
            space.append(board[row + ship_len][column])
    if "X" in space:
        print("Too close! Please enter a new coordinate.")
        return False
    else:
        return True

def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Fire in the hole!!')

def count_accurate_hit(board):
    count = 0
    for row in board:
        for column in row:
            if column =="H":
                count += 1
    return count

def turn(board):
    if board == player_1_guess:
        row, column = user_input(player_1_guess)
        if player_2[row][column] == "X":
            board[row][column] = "H"
        else:
            board[row][column] = "M"
    else:
        row, column = user_input(player_2_guess)
        if player_1[row][column] == "X":
            board[row][column] = "H"
        else:
            board[row][column] = "M"

place_ships(player_1)
place_ships(player_2)

while True:
    while True:
        print(bcolors.HEADER_1 + "\n\n\n\n\n\n\n\n\n\n Player_1 guessing a position of Player_2 ship!" + bcolors.END)
        display_board(player_1_guess)
        turn(player_1_guess)
        break
    display_board(player_1_guess)
    time.sleep(2)
    if count_accurate_hit(player_1_guess) == 10:
        print("Player 1 won")
        break
    while True:
        print(bcolors.HEADER_1 + "\n\n\n\n\n\n\n Player_2 guessing a position of Player_1 ship!" + bcolors.END)
        display_board(player_2_guess)
        turn(player_2_guess)
        break
    display_board(player_2_guess)
    time.sleep(2)
    if count_accurate_hit(player_2_guess) == 10:
        print("Player 2 won")
        break