num = int(input())
happyNumbers = [4,7]
count = 0
while count <= 7 and num != 0:
    if num % 10 in happyNumbers:
        count+=1
    num//=10
if count in happyNumbers:
    print("YES")
else:
    print("NO")
