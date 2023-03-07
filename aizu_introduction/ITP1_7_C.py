# 4 5
# 1 1 3 4 5
# 2 2 2 4 5
# 3 3 0 1 1
# 2 3 4 4 6

# 1 1 3 4 5 14
# 2 2 2 4 5 15
# 3 3 0 1 1 8
# 2 3 4 4 6 19
# 8 9 9 13 17 56


r, c = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(r)]

for index, _ in enumerate(table):
    table[index].append(sum(table[index]))

c_sum = [0]*c
for i in range(r):
    for j in range(c):
        c_sum[j] += table[i][j]

for t in table:
    print(*t)

c_sum.append(sum(c_sum))
print(*c_sum)
