input = open("input.txt", "r")
outputs = []
inputs = []
oneCount = 0
fourCount = 0
sevenCount = 0
eightCount = 0

for out in input:
    o = out.split(" | ")
    outputs.append((o[1].strip()).split(" "))
    inputs.append((o[0].strip()).split(" "))


for code in outputs:
    for num in code:
        if len(num) == 2:
            oneCount += 1
        elif len(num) == 4:
            fourCount += 1
        elif len(num) == 3:
            sevenCount += 1
        elif len(num) == 7:
            eightCount += 1
        else:
            pass


print(oneCount + fourCount + sevenCount + eightCount)
