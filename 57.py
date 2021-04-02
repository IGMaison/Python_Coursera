s = input()
c = 0
k = 0
sk = ""
l = len(s)
while k < l:
    if sk == s[k] and s[k] == " ":
        c = c + 1
    sk = s[k]
    k = k + 1
if s[0] == " ":
    c = c + 1
if s[-1] == " ":
    c = c + 1
if s[0] == " " and l < 2 or s.count(" ") == l:
    print(0)
else:
    print(s.count(" ") + 1 - c)
