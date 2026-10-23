mail = input("Email: ")
pas = input("Пароль: ")
mail_k = 0
mail_err = []
pas_k = 0
pas_err = []
symbols = "!@#$%^&*"
if mail.count("@") == 1:
    mail_k += 1
else:
    mail_err.append("x @ Встречается не ровно один раз")
if mail_k == 1:
    ind = mail.find("@")
    if mail[ind + 1:].count(".") >= 1:
        mail_k += 1
    else:
        mail_err.append("х . не встречается после @")
else:
    mail_err.append("х @ Нету в Email")
if mail[0] not in ["@", "."] and mail[-1] not in ["@", "."]:
    mail_k += 1
else:
    mail_err.append("x начинается или заканчивается на @ или .")
if 6 <= len(mail) <= 30:
    mail_k += 1
else:
    mail_err.append("x Email не подходит по длине")
if mail_k == 4:
    print(f"Email: {mail} → OK")
else:
    print(f"Email: {mail} →")
    for i in mail_err:
        print("  ", i)
if len(pas) >= 8:
    pas_k += 1
else:
    pas_err.append("x Длина пароля меньше 8")
for i in pas:
    if i.isdigit():
        pas_k ++ 1
        break
else:
    pas_err.append("x Цифр нет в пароле")
for i in pas:
    if i.isalpha() and i.isupper():
        pas_k ++ 1
        break
else:
    pas_err.append("x нет больших заглавных букв")
for i in pas:
    if i.isalpha() and i.islower():
        pas_k ++ 1
        break
else:
    pas_err.append("x в пароле нет строчных букв")
for i in pas:
    if i in symbols:
        pas_k ++ 1
        break
else:
    pas_err.append("x в пароле нет специальных символов")
if pas_k == 5:
    print(f"Пароль: {pas} → OK")
else:
    print(f"Пароль: {pas} →")
    for i in pas_err:
        print("  ", i)