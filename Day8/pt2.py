from typing import final


input = open("input.txt", "r")
outputs = []
inputs = []
sortedOutputs = []
sortedInputs = []


for out in input:
    o = out.split(" | ")
    outputs.append((o[1].strip()).split(" "))
    inputs.append((o[0].strip()).split(" "))


# Find which number each input cooresponds to, then add the sorted array to our sorted inputs array
for boob in inputs:
    arr = ["", "", "", "", "", "", "", "", "", ""]
    # Find the easy inputs first
    for code in boob:
        if len(code) == 2:
            arr[1] = code
        elif len(code) == 4:
            arr[4] = code
        elif len(code) == 3:
            arr[7] = code
        elif len(code) == 7:
            arr[8] = code
        else:
            pass

    # Now we find the rest using the known inputs
    for code in boob:
        if len(code) == 5:
            if code.find((arr[1])[0]) != -1 and code.find((arr[1])[1]) != -1:
                arr[3] = code
            else:
                count = 0
                for letter in arr[4]:
                    if code.find(letter) != -1:
                        count += 1
                    else:
                        pass

                if count == 3:
                    arr[5] = code
                elif count == 2:
                    arr[2] = code

        elif len(code) == 6:
            if code.find((arr[1])[0]) != -1 and code.find((arr[1])[1]) != -1:
                counts = 0
                for letter in arr[4]:
                    if code.find(letter) != -1:
                        counts += 1
                    else:
                        pass

                if counts == 4:
                    arr[9] = code
                elif counts == 3:
                    arr[0] = code
            else:
                arr[6] = code
    sortedInputs.append(arr)


i = 0
total = 0
for code in outputs:

    string = ""
    finalNum = []
    for num in code:
        count = [[0, 0], [0, 2], [0, 3], [0, 5], [0, 6], [0, 9]]
        if len(num) == 2 or len(num) == 4 or len(num) == 3 or len(num) == 7:
            if len(num) == 2:
                finalNum.append(1)
            elif len(num) == 4:
                finalNum.append(4)
            elif len(num) == 3:
                finalNum.append(7)
            elif len(num) == 7:
                finalNum.append(8)
        else:

            for letter in num:
                if (sortedInputs[i][0]).find(letter) != -1:
                    count[0][0] += 1
                if (sortedInputs[i][2]).find(letter) != -1:
                    count[1][0] += 1
                if (sortedInputs[i][3]).find(letter) != -1:
                    count[2][0] += 1
                if (sortedInputs[i][5]).find(letter) != -1:
                    count[3][0] += 1
                if (sortedInputs[i][6]).find(letter) != -1:
                    count[4][0] += 1
                if (sortedInputs[i][9]).find(letter) != -1:
                    count[5][0] += 1

            largestNum = [0, 0]
            for x in count:
                if largestNum == [0, 0]:
                    largestNum = x
                else:
                    if x[0] > largestNum[0]:
                        largestNum = x

            finalNum.append(largestNum[1])
    for a in finalNum:
        string += str(a)
    total += int(string)
    i += 1


print(total)
