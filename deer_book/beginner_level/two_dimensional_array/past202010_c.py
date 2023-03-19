# # 0:下、1:右、2:上、3:左、 4:右下、5：右上、6:左上、7:左下
# # import numpy as np
# DX = [0, 1, 0, -1, 1, 1, -1, -1]
# DY = [1, 0, -1, 0, 1, -1, -1, 1]


# 0:下、1:右、2:上、3:左、 4:右下、5：右上、6:左上、7:左下、8:現在地
# import numpy as np
DX = [0, 1, 0, -1, 1, 1, -1, -1, 0]
DY = [1, 0, -1, 0, 1, -1, -1, 1, 0]

n, m = map(int, input().split())

L = [input() for _ in range(n)]
result = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):

        for dx, dy in zip(DX, DY):
            nj, ni = j + dx, i + dy
            # チェック対象の隣接するマス目が、盤面外に出ていないかチェック
            # 横のマス目の数(nj)がn以上になっていたら、盤面外。縦のマス目の数(ni)がn以上になっていたら、盤面外。
            if nj < 0 or nj >= m or ni < 0 or ni >= n:
                continue

            if L[ni][nj] == "#":
                result[i][j] += 1

for k in result:
    print(*k, sep="")
