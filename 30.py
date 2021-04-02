a, b, c = int(input()), int(input()), int(input())
if a > c:
    a, c = c, a
if b > c:
    c, b = b, c
if b < a:
    a, b = b, a
print(a, b, c)
