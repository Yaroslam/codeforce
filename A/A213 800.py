count = int(input())
res = 0
for i in range(count):
    canSolve = map(int, input().split())
    if sum(canSolve) >= 2:
        res+=1
print(res)