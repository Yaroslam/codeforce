count = int(input())
lands = 0
prev = -1
for i in range(count):
    magnet = input()
    if prev == -1:
        prev = magnet[0]
    else:
        if prev != magnet[0]:
            lands+=1
        prev = magnet[0]
print(lands+1)