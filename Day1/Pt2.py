input = open("input.txt", "r")
list = []
previous = 0
count = 0
i = 0

for number in input:
    list.append(int(number.strip()))


for measurement in list:
    index = list.index(measurement)
    sum = measurement + list[i - 1] + list[i - 2]

    if measurement != 140 and measurement != 141:
        if previous == 0:
            i += 1
            previous = sum
        else:
            if sum > previous:
                count += 1
            i += 1
            previous = sum
    else:
        i += 1
print(count)
