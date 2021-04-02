def nod(n, m):
    if n < m:
        n, m = m, n
    if n % m == 0:
        return m
    return nod(m, n % m)


def reduceFraction(n, m):
    return int(n / nod(n, m)), int(m / nod(n, m))


n, m = int(input()), int(input())
print(*reduceFraction(n, m))
