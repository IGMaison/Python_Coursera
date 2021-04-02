lines = [0] * 101
inpLines = list(map(int, input().split()))
for i in inpLines:
    lines[i] += 1
for i in range(len(lines)):
    print((str(i) + " ") * lines[i], end='')
