magnets = int(input())
magnetsValue = []
for i in range(magnets):
    magnetPole = input()
    magnetsValue.append(magnetPole)
if magnets == 0:
    print(0)
groupCounter = 1
pole = magnetsValue[0]
for i in range(1,magnets):
    if magnetsValue[i] != pole:
        groupCounter += 1
        pole = magnetsValue[i]
print(groupCounter)