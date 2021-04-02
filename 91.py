n = int(input())
myList = []
for i in range(n):
    myList.append(tuple(input().split()))
myList.sort(key=lambda d: int(d[1]), reverse=True)
for i in myList:
    print(i[0])
