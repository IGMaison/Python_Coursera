a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    max = a
elif c < b:
    max = b
else:
    max = c
print(max)
