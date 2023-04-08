# import sys
# n, m = map(int, input().split())
# A = [list(map(int, input().split())) * m for _ in range(n)] * m
# q = int(input())

# sys.setrecursionlimit(1 << 20)

# done = False

# def dfs(tmp_s, tmp_t, cnt, flag, s, t):
#     global done
#     if done:
#         return cnt
#     if tmp_s == s and tmp_t == t:
#         done = True
#         return cnt

#     # print("aaaaaaaaaaaaa")
#     # print(A[tmp_s][tmp_t] == 1)
#     print(tmp_s, tmp_t)
#     # print(cnt)
#     print("----------")

#     if tmp_s < n*m and tmp_t < n*m and A[tmp_s][tmp_t] == 0 and A[tmp_s][tmp_t] == 0:
#         print(-1)

#     if tmp_s < n*m and tmp_s <= s and A[tmp_s][tmp_t] == 1:  # 下に移動する場合
#         if flag:
#             flag = False
#             cnt += 1
#         dfs(tmp_s + 1, tmp_t, cnt, flag, s, t)

#     if tmp_s < n*m and tmp_t <= t and A[tmp_s][tmp_t] == 1:  # 右に移動する場合
#         if not flag:
#             flag = True
#             cnt += 1
#         # print("bbbbbbbbbbbbb")
#         dfs(tmp_s, tmp_t + 1, cnt, flag, s, t)


# for i in range(q):
#     s, t = map(int, input().split())
#     s = s - 1
#     t = t - 1
#     cnt = 0

#     stack = []
#     tmp_s = 0
#     tmp_t = 0

#     flag = True

#     if s == 0 and A[tmp_s][tmp_t + 1] == 1:
#         flag = False

#     ans = dfs(tmp_s, tmp_t, cnt, flag, s, t)
#     print(ans)


# 他者の解答(全点対最短経路(ワーシャルフロイド法))
# 全点対最短経路問題(APSP)を解くアルゴリズム。
# グラフ 𝐺=(𝑉,𝐸)の全てのペア (𝑣,𝑤)間の最短経路コストを求める。
# see: https://atcoder.jp/contests/arc159/tasks/arc159_a
# 解答: https://atcoder.jp/contests/arc159/submissions/40411316
N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

INF = float('inf')
for i in range(N):
    for j in range(N):
        if A[i][j] == 0:
            A[i][j] = INF

for k in range(N):
    for i in range(N):
        for j in range(N):
            A[i][j] = min(A[i][j], A[i][k]+A[k][j])
Q = int(input())
for i in range(Q):
    s, t = map(int, input().split())
    s -= 1
    t -= 1
    s %= N
    t %= N
    if A[s][t] == INF:
        print(-1)
    else:
        print(A[s][t])
