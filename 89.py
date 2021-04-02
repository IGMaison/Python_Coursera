with open('input.txt', 'r', encoding='utf8') as readFile:
    lines = readFile.readlines()
for i in range(len(lines)):
    lines[i] = tuple(lines[i].split())
lines.sort()
with open('output.txt', 'w', encoding='utf8') as writeFile:
    for i in lines:
        print(i[0] + ' ' + i[1] + ' ' + i[3], file=writeFile)
