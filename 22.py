num = int(input())
num14 = (num // 1000 - num % 10) ** 2
num23 = (num // 100 % 10 - num // 10 % 10) ** 2
print(num14 + num23 + 1)
