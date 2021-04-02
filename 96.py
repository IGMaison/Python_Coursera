newList = list(map(int, input().split()))
newSet = set()
for i in newList:
    print("YES" if i in newSet else "NO")
    newSet.add(i)
