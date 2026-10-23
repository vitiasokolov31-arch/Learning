s = [int(i) for i in input().split() if i.isdigit()]
n = s[0]
k = s[1]
s = s[2:]
new = []
if k > n:
    k = k % 6
new += (s[-k:])
new += (s[:-k])
print(*new)

