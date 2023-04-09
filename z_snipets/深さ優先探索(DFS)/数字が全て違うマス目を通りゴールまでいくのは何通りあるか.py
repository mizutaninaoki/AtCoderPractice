# see: https://atcoder.jp/contests/abc293/tasks/abc293_c
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
