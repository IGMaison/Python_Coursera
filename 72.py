def IsPointInCircle(x, y, xc, yc, r):
    return ((x - xc) ** 2 + (y - yc) ** 2) ** 0.5 <= r


x, y, xc, yc, r = float(input()), float(input()), \
                  float(input()), float(input()), float(input())
if IsPointInCircle(x, y, xc, yc, r):
    print("YES")
else:
    print("NO")
