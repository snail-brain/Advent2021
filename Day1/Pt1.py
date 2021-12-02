input = open("input.txt", "r")
list = []
previous = 0
count = 0

for number in input:
    list.append(int(number.strip()))

for measurement in list:
    if previous == 0:
        previous = measurement
        pass
    if measurement > previous:
        count += 1
    previous = measurement


print(count)
