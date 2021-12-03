input = open("input.txt", "r")
list = []
gamma = ""
epsilon = ""


for number in input:
    list.append(number.strip())


def findCount(list):
    countOne = []
    countZero = []
    x = 0

    while x < 12:
        countOne.append(0)
        countZero.append(0)
        x += 1

    for number in list:
        i = 0
        while i < len(number):
            if number[i] == "0":
                countZero[i] = countZero[i] + 1
            else:
                countOne[i] = countOne[i] + 1
            i += 1
    return countZero, countOne


def createBinary(Zero, One):
    i = 0
    gammaRate = ""
    epsilonRate = ""

    while i < 12:
        if Zero[i] > One[i]:
            gammaRate = gammaRate + "0"
            epsilonRate = epsilonRate + "1"
            i += 1
        else:
            gammaRate = gammaRate + "1"
            epsilonRate = epsilonRate + "0"
            i += 1

    return (gammaRate, epsilonRate)


def binaryToDecimal(binary):
    total = 0
    for number in binary:
        total = (total * 2) + int(number)
    return total


def cyclePop(list, value, index):
    newList = []
    for number in list:
        if number[index] == value:
            newList.append(number)
    return newList


def findOxygen():
    listHere = list
    i = 0

    while len(listHere) > 1:
        zero, one = findCount(listHere)
        if int(zero[i]) > int(one[i]):
            listHere = cyclePop(listHere, "0", i)
        elif int(zero[i]) <= int(one[i]):
            listHere = cyclePop(listHere, "1", i)
        i += 1
    return listHere[0]


def findC02():
    listHere = list
    i = 0

    while len(listHere) > 1:
        zero, one = findCount(listHere)
        if int(zero[i]) <= int(one[i]):
            listHere = cyclePop(listHere, "0", i)
        elif int(zero[i]) > int(one[i]):
            listHere = cyclePop(listHere, "1", i)
        i += 1
    return listHere[0]


def main():
    print(binaryToDecimal(findC02()) * binaryToDecimal(findOxygen()))


main()
