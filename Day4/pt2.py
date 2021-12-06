import numpy as np


rnd = open("rndInput.txt", "r")
boards = open("boards.txt", "r")


# Create array of the given numbers
rndIn = ""
for number in rnd:
    rndIn = number
rndArray = rndIn.split(",")

# Create array of given game boards
hitMap = []
boardsArray = []
winningBoards = []
skip = 5
count = 0

for number in boards:
    # Skip empty lines
    if count == skip:
        skip = skip + 5
    else:
        # Remove extra spaces then add next array into board list
        edits = ((number.strip()).replace("  ", " ")).split(" ")
        boardsArray.append(edits)
        hitMap.append([0, 0, 0, 0, 0])
        count += 1

# Modify both hitmap and boards to be numpy 3d arrays
x = np.array(boardsArray).reshape(100, 5, 5)
newHitMap = np.array(hitMap).reshape(100, 5, 5)


def drawing(rnd):
    # For every number drawn...
    for drawing in rnd:
        boardCount = -1
        while boardCount < len(x) - 1:
            boardCount += 1
            rowCount = -1
            # Comb through each row of the current board
            while rowCount < 4:
                rowCount += 1
                columnCount = -1
                # Check if any number in each row equals the number drawn
                while columnCount < 4:
                    columnCount += 1
                    # If said number does equal the number drawn...
                    if int(x[boardCount, rowCount, columnCount]) == int(drawing):
                        # Mark on hitmap then check for bingo
                        newHitMap[boardCount, rowCount, columnCount] = 1
                        checkWin, winner = checkBingo()
                        # If there is a bingo...
                        # Return the winning board and the winning number
                        if checkWin:
                            if len(winningBoards) < 100:
                                pass
                            else:
                                return winner[0], int(drawing)


def checkBingo():
    i = 0
    # iterate through entire hitmap looking for a whole column or row to return true
    # return the winning row or column
    while i < 100:
        if i not in winningBoards:
            y = 0
            x = 0
            while y < 5:
                if all(newHitMap[i, y, :]):
                    winningBoards.append(i)
                    return True, [i, y, "y"]
                y += 1
            while x < 5:
                if all(newHitMap[i, :, x]):
                    winningBoards.append(i)
                    return True, [i, x, "x"]
                x += 1
            i += 1
        else:
            i += 1
    return False, 0


def finalScore(winningBoard, winningNum):
    sum = 0
    y = 0

    # iterate through the winning board
    # add up the sum of all unmarked spaces in said board
    while y < 5:
        z = 0
        while z < 5:
            if newHitMap[winningBoard, y, z] == 0:
                sum += int(x[winningBoard, y, z])
            z += 1
        y += 1
    return sum * winningNum


def main():
    winningBoard, winningNum = drawing(rndArray)
    print(finalScore(winningBoard, winningNum))


main()
