price, money, bananas = map(int, input().split())
needs = 0
for i in range(1, bananas + 1):
    needs += price * i
if money >= needs:
    print(0)
else:
    print(needs - money)
