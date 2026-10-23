line1, line2, line3 = [input() for i in range(3)]
if len(line2) == 0 and len(line3) == 0:
    print("Не хайку. Должно быть 3 строки.")
    exit()
gl = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
k1 = 0
k2 = 0
k3 = 0
for i in gl:
    k1 += line1.lower().count(i)
    k2 += line2.lower().count(i)
    k3 += line3.lower().count(i)
if k1 == 5 and k2 == 7 and k3 == 5:
    print("Хайку!")
else:
    print("Не хайку.")
