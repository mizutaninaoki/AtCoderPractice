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
