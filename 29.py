n = int(input())
if n % 10 == 1 and n != 11:
    print(n, "korova")
elif (10 > n or n > 14) and 2 <= n % 10 <= 4:
    print(n, "korovy")
else:
    print(n, "korov")
