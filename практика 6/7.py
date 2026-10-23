s = [i for i in input().split() if i.isalnum()]
n = s[0]
words = s[1:]
for i in words:
    if len(i) > 10:
        print(f"{i[0]}{len(i) - 2}{i[-1]}", end=' ')
    else:
        print(i, end=' ')