input = open("input.txt", "r")
lanternfish = []

for x in input:
    for fish in x.split(","):
        lanternfish.append(int(fish))


def propogate():
    i = 0
    # Do once every day through day 80
    while i < 80:
        x = 0
        initLength = len(lanternfish)
        for fish in lanternfish:
            if x < initLength:
                if fish == 0:
                    lanternfish[x] = 6
                    lanternfish.append(8)
                else:
                    lanternfish[x] -= 1
                x += 1
            else:
                pass
        i += 1
    return len(lanternfish)


print(propogate())
