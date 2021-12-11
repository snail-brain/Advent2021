from typing import Collection


input = open("input.txt", "r")
heightmap = []
lowPoints = []
total = 0

for line in input:
    heightmap.append(line.strip())
floor = heightmap.index(heightmap[-1])

i = 0
# Find each lowpoint and add coordinates to our lowPoints array
# We check to see if any points around the point we're checking are higher than og point
# Also need to make sure we're not checking an invalid array input, would happen if we're on a corner, or against an edge
for row in heightmap:
    x = 0
    if heightmap.index(row) == 0:
        for num in row:
            if x == 0:
                if (heightmap[i + 1])[0] > num and row[x + 1] > num:
                    lowPoints.append([num, i, x])
            elif x == len(row) - 1:
                if row[x - 1] > num and (heightmap[i + 1])[x] > num:
                    lowPoints.append([num, i, x])
            else:
                if (
                    row[x - 1] > num
                    and (heightmap[i + 1])[x] > num
                    and row[x + 1] > num
                ):
                    lowPoints.append([num, i, x])
            x += 1

    elif i == len(heightmap) - 1:
        for num in row:
            if x == 0:
                if (heightmap[i - 1])[0] > num and row[x + 1] > num:
                    lowPoints.append([num, i, x])
            elif x == len(row) - 1:
                if row[x - 1] > num and (heightmap[i - 1])[x] > num:
                    lowPoints.append([num, i, x])
            else:

                if (
                    row[x - 1] > num
                    and (heightmap[i - 1])[x] > num
                    and row[x + 1] > num
                ):
                    lowPoints.append([num, i, x])
            x += 1

    else:
        for num in row:
            if x == 0:
                if (
                    (heightmap[i - 1])[x] > num
                    and (heightmap[i + 1])[x] > num
                    and row[x + 1] > num
                ):
                    lowPoints.append([num, i, x])
            elif x == len(row) - 1:
                if (
                    (heightmap[i - 1])[x] > num
                    and (heightmap[i + 1])[x] > num
                    and row[x - 1] > num
                ):
                    lowPoints.append([num, i, x])
            else:
                if (
                    (heightmap[i - 1])[x] > num
                    and (heightmap[i + 1])[x] > num
                    and row[x - 1] > num
                    and row[x + 1] > num
                ):
                    lowPoints.append([num, i, x])
            x += 1
    i += 1


# Given a point, check all the points around it to see if they are part of the basin
def checkFourSquare(row, column):
    partsOfBasin = []

    # Find out if we're on an edge or not
    # There has to be a better way to do this right?
    # Checking if ceiling
    if row == 0:
        # Check if top-left corner
        if column == 0:
            if (heightmap[row + 1])[column] != "9":
                partsOfBasin.append([row + 1, column])
            if (heightmap[row])[column + 1] != "9":
                partsOfBasin.append([row, column + 1])
        # Check if top-right corner
        elif column == len(heightmap[0]) - 1:
            if (heightmap[row])[column - 1] != "9":
                partsOfBasin.append([row, column - 1])
            if (heightmap[row + 1])[column] != "9":
                partsOfBasin.append([row + 1, column])
        else:
            if (heightmap[row])[column + 1] != "9":
                partsOfBasin.append([row, column + 1])
            if (heightmap[row + 1])[column] != "9":
                partsOfBasin.append([row + 1, column])
            if (heightmap[row])[column - 1] != "9":
                partsOfBasin.append([row, column - 1])
    # Check if floor
    elif row == len(heightmap) - 1:
        # Check if bottom-left corner
        if column == 0:
            if (heightmap[row])[column + 1] != "9":
                partsOfBasin.append([row, column + 1])
            if (heightmap[row - 1])[column] != "9":
                partsOfBasin.append([row - 1, column])
        # Check if bottom-right corner
        elif column == len(heightmap[0]) - 1:
            if (heightmap[row])[column - 1] != "9":
                partsOfBasin.append([row, column - 1])
            if (heightmap[row - 1])[column] != "9":
                partsOfBasin.append([row - 1, column])
        else:
            if (heightmap[row])[column + 1] != "9":
                partsOfBasin.append([row, column + 1])
            if (heightmap[row])[column - 1] != "9":
                partsOfBasin.append([row, column - 1])
            if (heightmap[row - 1])[column] != "9":
                partsOfBasin.append([row - 1, column])

    else:
        # Check if left border
        if column == 0:
            if (heightmap[row])[column + 1] != "9":
                partsOfBasin.append([row, column + 1])
            if (heightmap[row + 1])[column] != "9":
                partsOfBasin.append([row + 1, column])
            if (heightmap[row - 1])[column] != "9":
                partsOfBasin.append([row - 1, column])
        # Check if right border
        elif column == len(heightmap[0]) - 1:
            if (heightmap[row])[column - 1] != "9":
                partsOfBasin.append([row, column - 1])
            if (heightmap[row + 1])[column] != "9":
                partsOfBasin.append([row + 1, column])
            if (heightmap[row - 1])[column] != "9":
                partsOfBasin.append([row - 1, column])
        else:
            if (heightmap[row])[column + 1] != "9":
                partsOfBasin.append([row, column + 1])
            if (heightmap[row])[column - 1] != "9":
                partsOfBasin.append([row, column - 1])
            if (heightmap[row + 1])[column] != "9":
                partsOfBasin.append([row + 1, column])
            if (heightmap[row - 1])[column] != "9":
                partsOfBasin.append([row - 1, column])

    return partsOfBasin


# Now that we have all of our lowPoints and a function to check for basins, we need to find the size of each basin
basins = []
for point in lowPoints:
    basinSize = 0

    toCheck = []
    checked = []
    for check in checkFourSquare(point[1], point[2]):
        if check not in toCheck:
            basinSize += 1
            toCheck.append(check)

    while toCheck != []:
        for point in toCheck:
            checked.append(point)
            toCheck.remove(point)

            for check in checkFourSquare(point[0], point[1]):
                if check not in checked and check not in toCheck:
                    basinSize += 1
                    toCheck.append(check)
    basins.append(basinSize)


topThree = [0, 0, 0]


# Find the top three biggest basins
for basin in basins:
    if basin > topThree[0]:
        topThree[2] = topThree[1]
        topThree[1] = topThree[0]
        topThree[0] = basin
    elif basin > topThree[1]:
        topThree[2] = topThree[1]
        topThree[1] = basin
    elif basin > topThree[2]:
        topThree[2] = basin
    else:
        pass


# Multiply the top three basins to find our answer
grandTotal = topThree[0] * topThree[1] * topThree[2]
print(grandTotal)
