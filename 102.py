import sys

myDict = {}
maxList = []
for word in sys.stdin.read().strip().split():
    myDict[word] = myDict.get(word, 0) + 1
    if myDict[word] > len(maxList):
        maxList.append(word)
    elif myDict[word] == len(maxList):
        if word < maxList[len(maxList) - 1]:
            maxList[len(maxList) - 1] = word
if len(maxList) == 0:
    print("")
else:
    print(maxList[len(maxList) - 1])

# Дан текст. Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше в лексикографическом
# порядке. key=lambda d: myDict.get(d)
