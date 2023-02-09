stops = int(input())
max = 0
curPeople = 0
for i in range(stops):
    leaves, entered = map(int, input().split())
    curPeople = curPeople - leaves + entered
    if curPeople >= max:
        max = curPeople
print(max)