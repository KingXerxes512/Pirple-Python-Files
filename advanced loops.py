evenRows = " |"
oddRows = "-"


def draw(rows, columns):
    if rows > 11 or columns > 11:
        print('Rows and Columns cannot exceed 11')
        return False

    for r in range(rows):
        if r % 2 == 0:
            print(evenRows * int(columns / 2), ' ')
        else:
            print(oddRows * columns)

    return True


# draw(11, 11)

currentField = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


# TicTacToe EXAMPLE
def drawField():
    for row in range(5):
        if row % 2 == 0:
            practicalRow = int(row / 2)
            for column in range(5):
                if column % 2 == 0:
                    practicalColumn = int(column / 2)
                    if column != 4:
                        print(currentField[practicalRow][practicalColumn], end="")
                    else:
                        print(currentField[practicalRow][practicalColumn])
                else:
                    print("|", end="")
        else:
            print("-----")
    print("")

