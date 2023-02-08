name = input()
symbols = []
for i in name:
    if i not in symbols:
        symbols.append(i)
if len(symbols) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
