a, b, i = int(input()), int(input()), 1
if a > b:
    i = -1
for i in range(a, b + i, i):
    print(i, end=" ")
