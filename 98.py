with open("input.txt", "r", encoding="utf8") as newFile:
    setYes = set(range(1, int(newFile.readline()) + 1))
    setNo = set()
    newList = list(newFile.readline().split())
    answer = newFile.readline().rstrip()
    while newList[0] != "HELP":
        if answer == "YES":
            setYes &= set(map(int, newList))
        else:
            setNo |= set(map(int, newList))
        newList = list(newFile.readline().split())
        answer = newFile.readline().rstrip()
print(*sorted(setYes - setNo))
