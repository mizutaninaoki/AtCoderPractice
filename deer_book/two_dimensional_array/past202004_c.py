n = int(input())
S = [input() for _ in range(n)]
S = list(reversed(S))

# 0:左上、1:上、2:右上(読み込みが逆順の条件があるため、指定上下も逆)
DX = [-1, 0, 1]
DY = [-1, -1, -1]

result = [["."]*(2*n-1) for _ in range(n)]

for i in range(n):
    for j in range(2*n-1):

        if S[i][j] == "#":
            result[i][j] = "#"
        elif S[i][j] == "X":
            result[i][j] = "X"
        elif S[i][j] == ".":
            continue

        for dx, dy in zip(DX, DY):
            nj, ni = j + dx, i + dy
            # チェック対象の隣接するマス目が、盤面外に出ていないかチェック
            # 横のマス目の数(nj)がn以上になっていたら、盤面外。縦のマス目の数(ni)がn以上になっていたら、盤面外。
            if nj < 0 or nj >= 2*n-1 or ni < 0 or ni >= n:
                continue

            if result[ni][nj] == "X":
                result[i][j] = "X"

for k in list(reversed(result)):
    print(*k, sep="")
