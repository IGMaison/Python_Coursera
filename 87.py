townCount = int(input())
townDistance = list(map(int, input().split()))
shelterCount = int(input())
shelterDistance = list(map(int, input().split()))
for i in range(len(townDistance)):
    townDistance[i] = [townDistance[i], i + 1]
for i in range(len(shelterDistance)):
    shelterDistance[i] = [shelterDistance[i], i + 1]
townDistance.sort()
shelterDistance.sort()
j = 0
for i in range(townCount):
    while j + 1 < len(shelterDistance) and \
            abs(townDistance[i][0] - shelterDistance[j][0]) >= \
            abs(townDistance[i][0] - shelterDistance[j + 1][0]):
        j += 1
    townDistance[i].append(shelterDistance[j][1])
    j -= 1
townDistance.sort(key=lambda d: d[1])
for i in range(len(townDistance)):
    print(townDistance[i][2], end=" ")
