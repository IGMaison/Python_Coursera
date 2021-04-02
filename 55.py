s = input()
pos1 = s.find("f")
pos2 = s.find("f", s.find("f") + 1)
if pos1 >= 0:
    if pos2 >= 0:
        print(pos2)
    else:
        print(-1)
else:
    print(-2)
