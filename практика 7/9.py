n,m = map(int, input().split())
matrix = [[1 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if i != 0 and j != 0:
            matrix[i][j] =  matrix[i - 1][j] + matrix[i][j - 1]
        print(str(matrix[i][j]).ljust(6), end=' ')
    print()
