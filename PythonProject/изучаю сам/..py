n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
k = 0
for i in range(n):
    for j in range(n):
        if i + j < n - 1:
            print(matrix[j + 1][i], end='')