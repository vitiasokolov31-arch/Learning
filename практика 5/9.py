s = input()
word = ""
if s[-1] != "#":
    print('Ошибка! Отсутствует символ #')
else:
    s = s[:-1]
    for i in range(1, len(s) + 1):
         if i % 2 != 0:
            word += s[i - 1]
    for i in range(len(s), 0, -1):
        if i % 2 == 0:
            word += s[i - 1]
    print(word)