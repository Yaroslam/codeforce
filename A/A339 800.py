math = input()
countOne = 0
countTwo = 0
countThree = 0
for i in math:
    if i == "1":
        countOne+=1
    elif i == "2":
        countTwo+=1
    elif i == "3":
        countThree+=1

resStr = ''
for i in range(countOne):
    resStr+="1+"
for i in range(countTwo):
    resStr+="2+"
for i in range(countThree):
    resStr+="3+"
print(resStr[:-1])
