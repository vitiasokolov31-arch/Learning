with open("Files/secret.txt") as f, \
     open("Files/secret_anonymized.txt", "w") as out:
    for line in f:
        name, phone, email = line.split(", ")
        tel, phone = phone.split(": ")
        phone = "*" * (len(phone) - 2) + phone[-2:]
        mail, email = email.split(": ")
        login, domain = email.split("@")
        email = login[0] + "***@" + domain
        out.write(f"{name}, {tel}: {phone}, {mail}: {email}\n")