s = [int(s[0]) for s in input().split()]
mx = -1
ind = []
numb = []
for i in range(len(s)):
    if i != 0 and i != len(s) - 1:
        if s[i] > s[i - 1] and s[i] > s[i + 1]:
            ind.append(s.index(s[i]))
            numb.append(s[i])
            if int(s[i]) > mx:
                mx = int(s[i])
print("Сокровища на индексах", *ind, "со значениями", *numb)
for x in s:
    if x != mx:
        print(x, end=' ')
    else:
        mx = -1

