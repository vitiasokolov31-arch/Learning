import random
s = []
while True:
    s.append(random.choice(["O", 'P']))
    if len(s) >= 3:
        if len(set(s[-3:])) == 1:
            print(*s, f"(попыток: {len(s)})")
            quit()
