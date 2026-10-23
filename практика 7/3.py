import random
n = int(input())
numbers = list(range(1, n ** 2 + 1))
matrix = [[0 for _ in range(n)] for _ in range(n)]
mag_const = n * (n ** 2 + 1) / 2
while True:
    k = 0
    random.shuffle(numbers)
    gl, pb, st, strk = 0, 0, 0, 0
    for i in range(n):
        for j in range(n):
            matrix[i][j] = numbers[k]
            if i == j:
                gl += matrix[i][j]
            if i + j == n - 1:
                pb += matrix[i][j]
            k += 1
        if sum(matrix[i]) == mag_const:
            strk += 1
    matrix_new = [[matrix[j][x] for j in range(n)] for x in range(n)]
    if gl == mag_const and pb == mag_const and strk == n and all(sum(matrix_new[z]) == mag_const for z in range(n)):
        for i in range(n):
            for j in range(n):
                print(matrix[i][j], end=' ')
            print()
        exit()




