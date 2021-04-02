max = 0
maxi = 0
n = -1
n2 = -1
while n != 0:
    n = int(input())
    if n == n2:
        maxi = maxi + 1
        if maxi > max:
            max = maxi
    elif n > 0:
        n2 = n
        maxi = 1
        if max == 0:
            max = 1
print(max)
