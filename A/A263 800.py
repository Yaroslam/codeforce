strPos = 0
colPos = 0
for i in range(5):
    string = list(map(int, input().split()))
    if 1 in string:
        strPos = i+1
        colPos = 0
        while string[colPos] != 1:
            colPos+=1
colPos+=1
res = abs(3 - colPos) + abs(3-strPos)
print(res)
