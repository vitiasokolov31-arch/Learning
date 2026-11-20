counts = {"INFO": 0, "WARNING": 0, "ERROR": 0, "CRITICAL": 0}

with open("Files/server_log.txt") as f:
    for line in f:
        parts = line.split(maxsplit=3)
        date, time, level, message = parts
        if level in counts:
            counts[level] += 1

for level, number in counts.items():
    print(f"{level}: {number}")