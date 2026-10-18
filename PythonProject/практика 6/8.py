k = 0
rooms = [int(x) for x in input().split() if x.isdigit()]
p, q = [rooms[i] for i in range(len(rooms)) if i % 2 == 0], [rooms[i] for i in range(len(rooms)) if i % 2 != 0]
for i in range(len(p)):
    if q[i] - p[i] >= 2:
        k += 1
print(k)