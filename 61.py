n = int(input())
if n > 0:
    for i in range(10 ** n - 1, 10 ** (n - 1) - 1, -2):
        print(i, end=" ")
