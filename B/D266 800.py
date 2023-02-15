def change_queue(queue):
    new_queue = ''
    i = 0
    while i <= len(queue) - 1:
        if i == len(queue)-1:
            new_queue += queue[i]
            i+=1
        elif queue[i] == "B" and queue[i + 1] == "G":
            new_queue += "G"
            new_queue += "B"
            i += 2
        else:
            new_queue += queue[i]
            i += 1
    return new_queue


queue_len, count = map(int, input().split())
queue = input()
for i in range(count):
    queue = change_queue(queue)
print(queue)
