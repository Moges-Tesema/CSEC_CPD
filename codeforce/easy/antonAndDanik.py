games = int(input())
result = input()
Anton = result.count("A")
Danik = result.count("D")
if Anton > Danik:
    print("Anton")
elif Danik > Anton:
    print("Danik")
else:
    print("Friendship")


