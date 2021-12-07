import numpy as np
from numpy.core.fromnumeric import shape

input = open("input.txt", "r")
inputLines = []
lineGraph = []

for line in input:
    x = ((line.replace(" -> ", ",")).strip()).split(",")
    inputLines.append(x)

newLines = (np.array(inputLines)).reshape(500, 2, 2)


def findLarge():
    i = 0
    largeX = 0
    largeY = 0
    while i < len(newLines):
        x = 0
        while x < 2:
            checkX = int(newLines[i, x, 0])
            checkY = int(newLines[i, x, 1])

            if checkX > largeX:
                largeX = checkX
            if checkY > largeY:
                largeY = checkY
            x += 1
        i += 1
    return largeX + 1, largeY + 1


largeX, largeY = findLarge()


for num in range(largeX * largeY):
    lineGraph.append(0)
newGraph = (np.array(lineGraph)).reshape(largeX, largeY)


def checkPlot():

    for tit in newLines:
        x1 = int(tit[0, 0])
        x2 = int(tit[1, 0])
        y1 = int(tit[0, 1])
        y2 = int(tit[1, 1])

        if x1 == x2:
            plotX(x1, y1, y2)
        elif y1 == y2:
            plotY(x1, x2, y1)
        else:
            plotDiag(x1, x2, y1, y2)


def plotX(x, y1, y2):
    if y1 >= y2:
        while y2 <= y1:
            newGraph[x, y2] += 1
            y2 += 1
    else:
        while y2 >= y1:
            newGraph[x, y2] += 1
            y2 -= 1


def plotY(x1, x2, y):
    if x1 >= x2:
        while x1 >= x2:
            newGraph[x1, y] += 1
            x1 -= 1
    else:
        while x1 <= x2:
            newGraph[x1, y] += 1
            x1 += 1


def plotDiag(x1, x2, y1, y2):
    # Four different directions a diagonal can go

    # Up left
    if x1 > x2 and y1 > y2:
        while x1 >= x2 and y1 >= y2:
            newGraph[x1, y1] += 1
            x1 -= 1
            y1 -= 1
    # Up right
    elif x1 < x2 and y1 > y2:
        while x1 <= x2 and y1 >= y2:
            newGraph[x1, y1] += 1
            x1 += 1
            y1 -= 1
    # Down left
    elif x1 > x2 and y1 < y2:
        while x1 >= x2 and y1 <= y2:
            newGraph[x1, y1] += 1
            x1 -= 1
            y1 += 1
    # Down right
    elif x1 < x2 and y1 < y2:
        while x1 <= x2 and y1 <= y2:
            newGraph[x1, y1] += 1
            x1 += 1
            y1 += 1


def twoLines():
    count = 0
    for arr in newGraph:
        for num in arr:
            if num >= 2:
                count += 1
    return count


def main():
    checkPlot()
    print(twoLines())


main()
