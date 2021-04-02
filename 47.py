n = float(input())
kop = int((n % 1 + .00005) * 100)
print(int(n // 1), kop)

# n = float(input())
# kop = str(int(n % 1 * 10)) + str(round(n % 1 * 100) - int(n % 1 * 10) * 10)
# if kop == "00":
#    kop = 0
# print(int(n // 1), " ", kop, sep="")
