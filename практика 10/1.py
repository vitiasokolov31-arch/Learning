count = 0
with open("Files/server_log.txt", "r", encoding="utf-8") as f, \
     open("Files/errors_only.txt", "w", encoding="utf-8") as out:
    for line in f:
        if "ERROR" in line or "CRITICAL" in line:
            out.write(line)
            count += 1
print(f"Найдено {count} критических ошибок")