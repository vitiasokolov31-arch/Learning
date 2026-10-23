s = [i for i in input().split() if i.isdigit()]
numb = s[0]
for i in s[1:]:
    if numb > i:
        print(s.index(i), end='')
        break
else:
    print(len(s))