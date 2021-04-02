def sum(a, b):
    if b == 0:
        return a
    return sum(a, b - 1) + 1


a, b = int(input()), int(input())
print(sum(a, b))
