input = open("input.txt", "r")
lanternfish = []
birthedSchools = []

for x in input:
    for fish in x.split(","):
        lanternfish.append(int(fish))


def propogate():
    i = 0
    # Do once every day through day 80
    while i < 256:
        fishNum = 0
        schoolNum = 0
        birthedCount = 0
        for fish in lanternfish:
            if fish == 0:
                lanternfish[fishNum] = 6
                birthedCount += 1
            else:
                lanternfish[fishNum] -= 1
            fishNum += 1

        for school in birthedSchools:
            if school[1] == 0:
                birthedCount += school[0]
                birthedSchools[schoolNum][1] = 6
            else:
                birthedSchools[schoolNum][1] -= 1
            schoolNum += 1

        birthedSchools.append([birthedCount, 8])
        i += 1

    totalFish = len(lanternfish)
    for school in birthedSchools:
        totalFish += school[0]

    return totalFish


print(propogate())
