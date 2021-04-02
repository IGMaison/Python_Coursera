a = list(map(int, input().split()))
max = min = 0
i = 1
while i < len(a):
    if a[min] > a[i]:
        min = i
    if a[max] < a[i]:
        max = i
    i += 1
a[max], a[min] = a[min], a[max]
print(*a)
