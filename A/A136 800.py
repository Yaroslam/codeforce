friends = int(input())
gifts = list(map(int, input().split()))
res = [0 for i in range(friends)]
count = 1
for i in gifts:
    res[i-1] = count
    count+=1
for i in res:
    print(i, end=' ')