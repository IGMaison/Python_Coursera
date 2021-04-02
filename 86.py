s_n = list(map(int, input().split()))
v = []
for i in range(s_n[1]):
    v.append(int(input()))
v.sort()
i = 0
d = 0
while i < len(v) and d + v[i] <= s_n[0]:
    d += v[i]
    i += 1
print(i)
