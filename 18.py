sec = int(input())
print(sec // 3600 % 24, ":",
      sec // 60 % 60 // 10, sec // 60 % 60 % 10, ":",
      sec % 60 // 10, sec % 60 % 10, sep="")
