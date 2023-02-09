word = input()
capital = 0
stroshnie = 0
for i in word:
    if 'a' <= i <= 'z':
        stroshnie+=1
    if 'A' <= i <= "Z":
        capital+=1
if capital > stroshnie:
    print(word.upper())
else:
    print(word.lower())