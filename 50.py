a, b, c = float(input()), float(input()), float(input())
d = b ** 2 - 4 * a * c
x1 = (-b + d ** .5) / 2 / a
x2 = (-b - d ** .5) / 2 / a
if d < 0:
    ()
elif x1 > x2:
    print(x2, x1)
elif d == 0:
    print(x1)
else:
    print(x1, x2)
