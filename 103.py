import sys

myDict = {}
for word in sys.stdin.read().strip().split():
    myDict[word] = myDict.get(word, 0) + 1
for i in sorted(sorted(myDict.items()), key=lambda d: d[1], reverse=True):
    print(i[0])

# Дан текст. Выведите все слова, встречающиеся в тексте, по одному на каждую
# строку. Слова должны быть отсортированы по убыванию их количества появления
# в тексте, а при одинаковой частоте появления — в
# лексикографическом порядке.
