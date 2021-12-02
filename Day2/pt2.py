input = open("input.txt", "r")
(direction, amount) = [], []
(horizontal, depth, aim) = 0, 0, 0
i = 0

for x in input:
    y = x.split(" ")
    direction.append(y[0])
    amount.append(int(y[1]))


for word in direction:
    number = amount[i]
    i += 1
    if word == "up":
        aim -= number
    elif word == "down":
        aim += number
    else:
        horizontal += number
        depth += aim * number
print(horizontal * depth)
