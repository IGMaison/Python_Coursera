n, a, x = int(input()), list(map(int, input().split())), int(input())
a.sort()
i = 0
while i < len(a) - 1 and abs(x - a[i]) >= abs(x - a[i + 1]):
    i += 1
print(a[i])
