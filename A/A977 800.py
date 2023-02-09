num, operations = map(int, input().split())
for i in range(operations):
    ostatok = num % 10
    if ostatok == 0:
        num//=10
    else:
        num-=1
print(num)