# 3 4
# 1 2 0 1
# 0 3 0 1
# 4 1 1 0
# 1
# 2
# 3
# 0


# 5
# 6
# 9



n, m = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(n)]
b = [int(input()) for _ in range(m)]

for i in range(n):
    count = 0

    for j in range(m):
        count += A[i][j] * b[j]
    print(count)