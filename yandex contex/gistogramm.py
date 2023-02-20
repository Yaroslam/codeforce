file1 = open("input.txt", "r")
symbols = {}
maximum = 0

while True:
    line = file1.readline()

    for i in line.strip():
        if i == " ":
            continue
        elif i not in symbols.keys():
            symbols[i] = 1
        else:
            symbols[i] += 1
    if not line:
        break

file1.close()
maximum = max(symbols.values())
symbols = dict(sorted(symbols.items(), key=lambda x: x[0]))
for i in symbols:
    if symbols[i] >= maximum:
        maximum = symbols[i]
supMax = maximum
for i in range(maximum):
    for i in symbols:
        if symbols[i] == supMax:
            symbols[i] -= 1
            print("#", end='')
        else:
            print(' ', end='')
    supMax -= 1
    print("")
for i in symbols:
    print(i, end='')
