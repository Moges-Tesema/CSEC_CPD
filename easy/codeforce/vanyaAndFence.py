friends, fanceHieght = list(map(int,input().split()))
friendsHieght = list(map(int,input().split()))
roadWidth = 0
for hieght in friendsHieght:
    if hieght > fanceHieght:
        roadWidth += 2
    else:
        roadWidth += 1
print(roadWidth)
