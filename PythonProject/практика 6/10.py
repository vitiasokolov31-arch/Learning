n, k = [int(i) for i in input().split()]
pos = 0
s = list(range(1, n + 1))
while len(s) > 1:
    pos = (pos + k - 1) % len(s)
    print(s.pop(pos), end=' ')
print('/',s[0])