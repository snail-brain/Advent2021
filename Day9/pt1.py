input = open("input.txt", "r")
heightmap = []
lowPoints = []
total = 0

for line in input:
    heightmap.append(line.strip())
floor = heightmap.index(heightmap[-1])

i = 0
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

for point in lowPoints:
    total += int(point[0]) + 1

print(lowPoints)
