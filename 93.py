def prohBal(arr):
    if len(arr) <= vocations:
        return 0
    if arr[0] == arr[vocations]:
        return 1
    if arr[vocations] == arr[vocations - 1]:
        i = vocations - 2
        while arr[i] == arr[vocations - 1]:
            i -= 1
        return arr[i]
    return array[vocations - 1]


with open("input.txt", "r", encoding="utf8") as rFile:
    array = []
    vocations = int(rFile.readline())
    for line in rFile:
        currLine = line.split()
        if int(currLine[-1]) >= 40 and int(currLine[-2]) >= 40 \
                and int(currLine[-3]) >= 40:
            array.append(int(currLine[-1]) + int(currLine[-2]) +
                         int(currLine[-3]))

array.sort(reverse=True)
prBal = prohBal(array)
with open("output.txt", 'w', encoding="utf8") as wFile:
    print(prBal, file=wFile)
