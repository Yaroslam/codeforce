countStones = int(input())
stones = input()
res = 0
for i in range(len(stones)-1):
    if stones[i] == stones[i+1]:
      res+=1
print(res)