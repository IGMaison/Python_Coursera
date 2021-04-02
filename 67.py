l = list(map(int, input().split()))
k = 0
for i in range(len(l) - 1):
    if l[k] <= l[i + 1]:
        k = i + 1
print(l[k], k)
