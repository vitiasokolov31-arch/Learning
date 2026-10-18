s = [i for i in input() if i.isalnum()][1:]
cord = [0, 0]
for i in s:
    if i == 'U':
        cord[1] += 1
    elif i == 'D':
        cord[1] -= 1
    elif i == 'L':
        cord[0] -= 1
    elif i == 'R':
        cord[0] += 1
print(*cord, '/', sum([abs(i) for i in cord]))
