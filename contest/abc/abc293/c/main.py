# 3 3
# 3 2 2
# 2 1 3
# 1 5 4


# 3


# --------------------------
# 正解のコード(深さ探索優先, dfsを使っている)
# --------------------------
import sys
sys.setrecursionlimit(1 << 20)

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

visited = set()
count = 0


def dfs(i, j):
    if i == H-1 and j == W-1:  # 終点に到達したら探索終了
        global count
        count += 1
        return
    visited.add(A[i][j])
    if i < H-1 and A[i+1][j] not in visited:  # 下に移動する場合
        dfs(i+1, j)
    if j < W-1 and A[i][j+1] not in visited:  # 右に移動する場合
        dfs(i, j+1)
    visited.remove(A[i][j])


dfs(0, 0)
print(count)


# from itertools import product
# from scipy.special import comb
# h, w = map(int, input().split())

# l = [list(map(int, input().split())) for _ in range(h)]

# print(l)
# for i in h:
#     for j in w:

# [0,0,1,1]
# [1,0,0,1]

# h2 = [0]*(len(h)-1)
# w2 = [1]*(len(w)-1)

# while True:
#   l2 = [0]*(h+w-1)
# #   for i in h:
# #     for j in w:
# #         l2[] = l[][]

#   h2[i] = 1
#   w2[i] = 0
#   for i in h2:
#       for j in w2:
#           l2[] = l[][]


# base = comb(5, 3, exact=True)
# print(base)  # 10


# for i in range(h):

#     for j in range(w):


# from itertools import combinations
# base = list(combinations("abcde",3))

# l = ['a', 'b', 'c', 'd']
# c = combinations(l, 2)


# ll = list(product(*l))
