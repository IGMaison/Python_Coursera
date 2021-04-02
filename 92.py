with open('92.txt', 'r', encoding='utf8') as rFile:
    resList = rFile.readlines()
for i in range(len(resList)):
    resList[i] = tuple(resList[i].split())
print(*resList)
