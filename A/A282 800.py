count = int(input())
res = 0
for i in range(count):
    sentece = input()
    if "-" in sentece:
       res-=1
    else:
        res+=1
print(res)