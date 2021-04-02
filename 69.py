l = list(map(int, input().split()))
min = 0
for i in range(1, len(l)):
    if l[min] > l[i] > 0 or l[min] <= 0:
        min = i
if l[min] > 0:
    print(l[min])
