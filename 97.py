with open("input.txt", "r", encoding="utf8") as newFile:
    newSet = set(newFile.read().split())
print(len(newSet))
