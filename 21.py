#h = int(input())
#a = int(input())
#b = int(input())
#print(-((b - h) // (a - b)))
import random

i = 0
while (i < 10):
    h = random.randint(10, 30)
    a = random.randint(2, h // 2)
    b = random.randint(0, a - 1)
    print(h, a, b, "->", -((b - h) // (a - b)))

    i = i + 1
