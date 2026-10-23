import math
n = int(input())
cords = [[]]
for i in range(n):
    cords[i].extend(list(map(int ,input().split())))
    if i != n - 1:
        cords.append([])
sanya_cords = list(map(int, input().split()))
min = 10
closest = None
for i in cords:
    if math.dist(sanya_cords, i) < min:
        min = math.dist(sanya_cords, i)
        closest = i
print("Ближайшее сокровище:", *closest)
print(f"Расстояние: {min:.2f}")
