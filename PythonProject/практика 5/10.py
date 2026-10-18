s = input()
word = []
for i in s:
    if i.isupper():
        word.append("_")
        word.append(i.lower())
    else:
        word.append(i)
print(*word, sep='')

