max = 0
n = -1
i = 0
while n != 0:
    n = int(input())
    if n > max:
        max = n
        i = 1
    elif n == max:
        i = i + 1
print(i)
