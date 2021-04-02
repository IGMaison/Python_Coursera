n = int(input())
f = "+___ ", "|__\ ", "|    "
print(f[0] * n)
for n in range(1, n + 1):
    print("|" + str(n) + " / ", end="")
print("", f[1] * n, f[2] * n, sep="\n")
