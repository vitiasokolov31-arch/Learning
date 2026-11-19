count = 0
with open("server_log.txt") as f:
    for line in f:
        if "ERROR" in line or "CRITICAL" in line:
            count += 1
print(f"Найдено {count} критических ошибок")