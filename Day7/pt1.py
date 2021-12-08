input = open("input.txt", "r")
crabs = []


for crab in input:
    crabs = crab.split(",")
count = 0
for crab in crabs:
    crabs[count] = int(crab)
    count += 1

fewestFuel = [0, 0]


i = 0
for crab in crabs:
    totalFuel = 0
    for crab in crabs:
        totalFuel += abs(crab - i)
    if fewestFuel[0] == 0:
        fewestFuel = [totalFuel, i]
    else:
        if fewestFuel[0] > totalFuel:
            fewestFuel = [totalFuel, i]
        else:
            pass
    i += 1

print(fewestFuel)
