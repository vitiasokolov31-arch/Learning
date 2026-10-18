mes = input("Введите сообщение: ")
gl = ["a","e","i","o","u"]
while True:
    k_gl = 0
    choice = int(input("Выберите действие (1–11): "))
    if 1 <= choice <= 11:
        match choice:
            case 1:
                pal = ''
                for i in mes[:]:
                    if i.isalpha():
                        pal += i
                if pal.lower() == pal[::-1].lower():
                    print("Сообщение является палиндромом!")
                else:
                    print("Сообщение не является палиндромом!")
            case 2:
                for i in mes:
                    if i in gl:
                        k_gl += 1
                print(k_gl)
            case 3:
                for j in mes:
                    if j.isdigit():
                        continue
                    else:
                        print("Не только цифры")
                        break
                else:
                    print("Только цифры")
            case 4:
                for j in mes:
                    if j.isalpha():
                        continue
                    else:
                        print("Не только буквы")
                        break
                else:
                    print("Только буквы")
            case 5:
                print(mes[::-1])
            case 6:
                print(mes.upper())
            case 7:
                print(mes.lower())
            case 8:
                new_mes = ''
                for i in mes:
                    if i == " ":
                        new_mes += "_"
                    else:
                        new_mes += i
                print(new_mes)
            case 9:
                r = 0
                for i in mes:
                    if i == "@":
                        r += 1
                    if r == 1 and i == ".":
                        r += 1
                if r == 2:
                    print("Коректный email")
                else:
                    print("Некоректный email")
            case 10:
                if "@" in mes:
                    ind = mes.index("@")
                    print(f"Домен: {mes[ind + 1:]}")
                else:
                    print("@ Нету в строке")
            case 11:
                    exit()
    else:
        print("Неверное число")
