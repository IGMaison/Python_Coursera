a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print(3)
elif b == c or a == c or a == b:
    print(2)
else:
    print(0)
