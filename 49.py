p, x, y = int(input()), int(input()), int(input())
fin = (x * 100 + y) * (100 + p) / 10000
kop = int((fin % 1 + .00005) * 100)
print(int(fin // 1), kop)
