resArr = []
res = 10000
count = int(input())
for i in range(count):
    res = 10000
    budilnikCount, hours, minutes = map(int, input().split())
    sleep = hours * 60 + minutes
    for j in range(budilnikCount):
        hours, minutes = map(int, input().split())
        budilnik = hours * 60 + minutes

        if budilnik - sleep < 0:
            if budilnik - sleep + 1440 < res:
                res = budilnik - sleep + 1440
        else:
            if budilnik - sleep < res:
                res = budilnik - sleep
    resArr.append(res)
for i in resArr:
    print(i//60, i%60)
# print(calculate([10, 30], [23, 35]))
