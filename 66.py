l = list(map(int, input().split()))
odd = 0
for i in range(0, len(l)):
    if l[i] > 0:
        odd = odd + 1
print(odd)
