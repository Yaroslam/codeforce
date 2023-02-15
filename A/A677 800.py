count, height = map(int, input().split())
friends = list(map(int, input().split()))
res = 0
for i in friends:
    if i > height:
        res+=2
    else:
        res+=1
print(res)
