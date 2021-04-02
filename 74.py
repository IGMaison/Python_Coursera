def IsPrime(n):
    if n % 2 == 0 and n != 2 or n == 1:
        return False
    i = 3
    while i <= n ** 0.5:
        if n % i == 0:
            return False
        i += 2
    return True


n = int(input())
if IsPrime(n):
    print("YES")
else:
    print("NO")
