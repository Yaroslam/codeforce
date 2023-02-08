count, place = canSolve = map(int, input().split())
score = list(map(int, input().split()))
borderScore = score[place - 1]
res = 0
for i in score:
    if i >= borderScore and i > 0:
        res += 1
print(res)
