card = [int(x) for x in input()]
chet = 0
nechet = 0
for i in range(len(card)):
    x = int(card[i])
    if i % 2 == 0:
        nechet += x * 2
        if x * 2 > 9:
            nechet -= 9
    if i % 2 != 0:
        chet += x
if (chet + nechet) % 10 == 0:
    print("Корректный номер")
else:
    print("Некорректный номер")