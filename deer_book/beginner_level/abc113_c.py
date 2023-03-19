# -----------------------------------
# 自分の解答(WA)
# -----------------------------------
# n, m = map(int, input().split())
# l = sorted([list(map(int, input().split()))
#            for i in range(m)], reverse=True, key=lambda x: (x[1]))

# tmp = []
# prev_p = None
# prev_index = 0
# for (p, y) in l:
#     p, y = str(p), str(y)
#     if prev_p != p:
#         prev_index = 0
#     prev_p = p

#     if len(p) < 6:
#         p = "0" * (6 - len(p)) + p

#     prev_index += 1
#     y = str(prev_index)

#     if len(y) < 6:
#         y = "0" * (6 - len(y)) + y

#     print(p+y)


# -----------------------------------
# 他者の解答(わからない。理解できない。。。)
# -----------------------------------
from collections import defaultdict
N, M = map(int, input().split())

P = []
C = [[] for _ in range(N+1)]

for _ in range(M):
    p, y = map(int, input().split())
    C[p].append(y)
    P.append((p, y))

for c in range(1, N+1):
    C[c] = {x: i for i, x in enumerate(sorted(C[c]), 1)}

for p, y in P:
    print(str(p).zfill(6) + str(C[p][y]).zfill(6))


# -----------------------------------
# 他者の解答２(わからない。理解できない。。。)
# -----------------------------------
# -*- coding: utf-8 -*-
n, m = map(int, input().split())

kens = defaultdict(list)

for i in range(m):
    p, y = map(int, input().split())
    kens[p].append([y, i])

result = [0] * m
for ken, v in kens.items():
    v.sort(key=lambda x: x[0])
    new = []
    for i, (year, index) in enumerate(v):
        i = str(i+1).zfill(6)
        ken = str(ken).zfill(6)
        tmp = (ken+i)
        result[index] = tmp

for i in range(m):
    print(result[i])
