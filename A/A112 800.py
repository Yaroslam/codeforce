firstStr = input()
secondStr = input()
res = 0

firstStr = firstStr.upper()
secondStr = secondStr.upper()

for i in range(len(firstStr)):
    if firstStr[i] != secondStr[i]:
        if firstStr[i] > secondStr[i]:
            res = 1
        elif firstStr[i] < secondStr[i]:
            res = -1
        break
print(res)