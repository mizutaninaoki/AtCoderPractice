# r, c = map(int, input().split())
# L = [input() for _ in range(r)]

# LC = L.copy()
# for i in LC:
#     for idx, j in enumerate(i):
#         try:
#             num = int(j)
#             left_idx = idx - num
#             right_idx = idx + num
#             # print(max(0, idx - num))
#             i[max(0, left_idx):idx] = "."
#             i[idx+1:min(len(j), right_idx + 1)] = "."
#             # print(LC[i][0:num])
#             print("------------")
#             print(j)
#             print("------------")

#         except:
#             continue

#             # # # 転置
#             # LC = list(zip(*LC))

#             # for k in LC:
#             #     for idx_m, m in enumerate(i):
#             #         try:
#             #             num = int(m)
#             #             left_idx = idx_m - num
#             #             right_idx = idx_m + num
#             #             k[max(0, left_idx):m] = "."
#             #             k[j+1:min(len(k), right_idx + 1)] = "."
#             #         except:
#             #             continue

#             # # 転置
#             # LC = list(zip(*LC))

#             # for p in range(r):
#             #     for q in range(c):
#             #         try:
#             #             num = int(L[i][j])

#             #             manhattan = num // 2

#             #             DX = [0]
#             #             DY = [0]
#             #             for o in range(manhattan):
#             #                 DX += [o, o, -o, -o]
#             #                 DY = [o, -o, -o, o]

#             #             for dx, dy in zip(DX, DY):
#             #                 nj, ni = q + dx, p + dy
#             #                 # チェック対象の隣接するマス目が、盤面外に出ていないかチェック
#             #                 # 横のマス目の数(nj)がn以上になっていたら、盤面外。縦のマス目の数(ni)がn以上になっていたら、盤面外。
#             #                 if ni < 0 or ni >= r or nj < 0 or nj >= c:
#             #                     continue

#             #                 if L[ni][nj] == "#":
#             #                     LC[p][q] = "."
#             #         except:
#             #             continue

#             for t in LC:
#                 print(*t, sep="")

# --------------------------------
# 他者の回答
# --------------------------------
R, C = map(int, input().split())
B = [list(input()) for _ in range(R)]

for i in range(R):
    for j in range(C):
        x = B[i][j]
        # それぞれのマスまでループして、そこからまた全体的にループで周り、マンハッタン距離の範囲内かどうか調べて、該当すればピリオドに変更する
        for k in range(R):
            for l in range(C):
                # マス目の文字が数字の時のみint型に変換して、マンハッタン距離と比較
                d = int(B[k][l]) if B[k][l].isdigit() else -1
                if abs(i-k) + abs(j-l) <= d:
                    x = "."
        print(x, end="")
    print()
