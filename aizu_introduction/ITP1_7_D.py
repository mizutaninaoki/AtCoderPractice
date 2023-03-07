# 3 2 3
# 1 2
# 0 3
# 4 5
# 1 2 1
# 0 3 2

# 1 8 5
# 0 9 6
# 4 23 14


n, m, l = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(m)]

for i in range(n):
    row = []
    for j in range(l):
        tmp = 0
        for k in range(m):
            tmp += A[i][k]*B[k][j]
        row.append(tmp)
    print(*row)