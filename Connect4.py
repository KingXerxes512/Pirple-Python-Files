import sys
from termcolor import colored, cprint

currentBoard = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ']]


# Draws the current state of the 'currentBoard' list of lists
def drawBoard():
    for row in range(12):
        if row % 2 == 0:
            practical_row = int(row / 2)
            for column in range(13):
                if column % 2 == 0:
                    practical_column = int(column / 2)
                    if column != 12:
                        print(currentBoard[practical_row][practical_column], end="")
                    else:
                        print(currentBoard[practical_row][practical_column])
                else:
                    print("|", end="")
        else:
            print("-------------")
    print("")


# Finds the bottom element of the column given by the player
def FindBottom(column, player_token):
    if column > 7:  # Check for valid input
        return False
    found_space = False
    for lists in currentBoard:  # Runs through board to see if there are remaining spaces
        for i in lists:
            if i == ' ':
                found_space = True
    prev_list = []
    for currentList in currentBoard:
        if currentList[column - 1] != ' ':  # This means we found a point which has been occupied
            if not prev_list:  # Checks if the player is putting token into full slot
                if not found_space:
                    return 'No More Moves'  # Returns if there are no remaining moves
                return False
            prev_list[column - 1] = player_token  # Set the spot 'above' to the player token
            return True  # Return is not import but more that we get out of the function at this point
        prev_list = currentList
    prev_list[column - 1] = player_token  # If we get to this point, we've reached the bottom and found no tokens
    return True


# Will run through possible methods of winning the game and return True if one of these is met
def HasPlayerWon():
    # Horizontal Victories
    for current_list in currentBoard:
        horizontal_test1 = current_list[0] == current_list[1] == current_list[2] == current_list[3] != ' '
        horizontal_test2 = current_list[1] == current_list[2] == current_list[3] == current_list[4] != ' '
        horizontal_test3 = current_list[2] == current_list[3] == current_list[4] == current_list[5] != ' '
        horizontal_test4 = current_list[3] == current_list[4] == current_list[5] == current_list[6] != ' '
        if horizontal_test1 or horizontal_test2 or horizontal_test3 or horizontal_test4:
            return True

    # Vertical Victories
    count = 0
    while count < 6:
        vertical_test1 = currentBoard[0][count] == currentBoard[1][count] == currentBoard[2][count] == \
                         currentBoard[3][count] != ' '
        vertical_test2 = currentBoard[1][count] == currentBoard[2][count] == currentBoard[3][count] == \
                         currentBoard[4][count] != ' '
        vertical_test3 = currentBoard[2][count] == currentBoard[3][count] == currentBoard[4][count] == \
                         currentBoard[5][count] != ' '
        if vertical_test1 or vertical_test2 or vertical_test3:
            return True
        else:
            count += 1

    # Diagonal Victories
    count = 0
    while count < 3:  # Checks for downward diagonal
        diagonal_test1 = currentBoard[0 + count][0] == currentBoard[1 + count][1] == currentBoard[2 + count][2] == \
                         currentBoard[3 + count][3] != ' '
        diagonal_test2 = currentBoard[0 + count][1] == currentBoard[1 + count][2] == currentBoard[2 + count][3] == \
                         currentBoard[3 + count][4] != ' '
        diagonal_test3 = currentBoard[0 + count][2] == currentBoard[1 + count][3] == currentBoard[2 + count][4] == \
                         currentBoard[3 + count][5] != ' '
        diagonal_test4 = currentBoard[0 + count][3] == currentBoard[1 + count][4] == currentBoard[2 + count][5] == \
                         currentBoard[3 + count][6] != ' '
        if diagonal_test1 or diagonal_test2 or diagonal_test3 or diagonal_test4:
            return True
        else:
            count += 1
    count = 0
    while count < 3:  # Checks for upward diagonal
        diagonal_test1 = currentBoard[5 - count][0] == currentBoard[4 - count][1] == currentBoard[3 - count][2] == \
                         currentBoard[2 - count][3] != ' '
        diagonal_test2 = currentBoard[5 - count][1] == currentBoard[4 - count][2] == currentBoard[3 - count][3] == \
                         currentBoard[2 - count][4] != ' '
        diagonal_test3 = currentBoard[5 - count][2] == currentBoard[4 - count][3] == currentBoard[3 - count][4] == \
                         currentBoard[2 - count][5] != ' '
        diagonal_test4 = currentBoard[5 - count][3] == currentBoard[4 - count][4] == currentBoard[3 - count][5] == \
                         currentBoard[2 - count][6] != ' '
        if diagonal_test1 or diagonal_test2 or diagonal_test3 or diagonal_test4:
            return True
        else:
            count += 1
    return False  # If the function gets to this point, then all the tests have failed and there is no winner yet


# Game Loop
playerWon = False
players = {1: colored('O', 'red'), 2: colored('O', 'yellow')}
currentPlayer = 2
drawBoard()
while not playerWon:
    valid_move = False
    if currentPlayer == 1:
        currentPlayer = 2
    else:
        currentPlayer = 1
    while not valid_move:
        move = int(input("Enter the column (1 - 7) that you would like to place your token: "))
        valid_move = FindBottom(move, players[currentPlayer])
        if valid_move == 'No More Moves':
            break
        if not valid_move:
            print("That column is full. Choose another!")
    if valid_move == 'No More Moves':
        currentPlayer = 3
        break
    drawBoard()
    playerWon = HasPlayerWon()
if currentPlayer == 3:
    print("THERE IS NO WINNER")
else:
    print("CONGRATULATIONS PLAYER {}, YOU'VE WON!!".format(currentPlayer))
