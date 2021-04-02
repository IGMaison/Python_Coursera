def MinDivisor(n):
    if n % 2 == 0:
        return 2
    i = 3
    while i <= n ** 0.5:
        if n % i == 0:
            return i
        i += 2
    return n


n = int(input())
print(MinDivisor(n))
