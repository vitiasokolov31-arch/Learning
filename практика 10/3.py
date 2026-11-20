people = []
with open("Files/olimp.txt") as f:
    for line in f:
        parts = line.split()
        surname, name, score = parts[0], parts[1], int(parts[2])
        people.append((surname, name, score))

mx = max(p[2] for p in people)
mx2 = max(p[2] for p in people if p[2] < mx)

for surname, name, score in people:
    if score == mx2:
        print(surname, name, score)