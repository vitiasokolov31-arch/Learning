def finding_minimum_row(row, k):
    count = 0
    for x in row:
        if x == 0:
            count += 1
        else:
            count = 0
        if count == k:
            return True

n,m = map(int, input().split())
cinema = [[None for _ in range(n)] for _ in range(n)]
k = int(input())

for i in range(n):
    cinema[i] = list(map(int, input().split()))
    if finding_minimum_row(cinema[i], k):
        print(f"\n{i + 1}")
        exit()

