N = int(input())
l = 0
for i in range(1, N + 1):
    k = len(str(i))
    sm = 0
    for j in str(i):
        sm += (int(j) ** k)
    if sm == i:
        l += 1
print(l)
