input = open("input.txt", "r")
list = []
gamma = ""
epsilon = ""


for number in input:
    list.append(number.strip())


def findCount():
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
            epsilonRate = epsilonRate + "2"
            i += 1

    epsilonRate = epsilonRate.replace("2", "0")
    return (gammaRate, epsilonRate)


def binaryToDecimal(binary):
    total = 0
    for number in binary:
        total = (total * 2) + int(number)
    return total


def main():
    (zero, one) = findCount()
    gamma, epsilon = createBinary(zero, one)
    gammaDecimal = binaryToDecimal(gamma)
    epsilonDecimal = binaryToDecimal(epsilon)
    print(gammaDecimal * epsilonDecimal)


main()
