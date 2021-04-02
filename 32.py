a, b, c, d, e, f = int(input()), int(input()), int(input()), \
                   int(input()), int(input()), int(input())
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
if b < a:
    b, a = a, b
if d > f:
    d, f = f, d
if e > f:
    e, f = f, e
if e < d:
    e, d = d, e
if a == d and b == e and c == f:
    print("Boxes are equal")
elif a <= d and b <= e and c <= f:
    print("The first box is smaller than the second one")
elif a >= d and b >= e and c >= f:
    print("The first box is larger than the second one")
else:
    print("Boxes are incomparable")
