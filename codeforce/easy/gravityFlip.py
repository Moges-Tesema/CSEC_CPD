columuns = int(input())
columunValues = list(map(int, input().split()))
columunValues.sort()
result = " ".join(map(str,columunValues))
# for i in range(len(columunValues)):
#     if i == 0:
#         result +=  str(columunValues[i])
#     else:
#         result += " " + str(columunValues[i])
print(result)