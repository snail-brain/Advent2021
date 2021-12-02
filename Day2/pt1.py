input = open("input.txt", "r")
direction = []
amount = []
horizontal = 0
depth = 0
i = 0

for x in input:
    y = x.split(" ")
    direction.append(y[0])
    amount.append(int(y[1]))


for word in direction:
    number = amount[i]
    i += 1
    if word == "up":
        depth -= number
    elif word == "down":
        depth += number
    else:
        horizontal += number
print(horizontal * depth)
