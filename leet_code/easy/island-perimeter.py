# see: https://leetcode.com/problems/island-perimeter/description/
# 自分の解答(DX, DYをあらかじめ定義して解く方法)
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # ---------------------------
        # 現在地を含める場合
        # ---------------------------
        # 0:下、1:右、2:上、3:左
        DX = [0, 1, 0, -1]
        DY = [1, 0, -1, 0]
        ans = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                for dx, dy in zip(DX, DY):
                    nj, ni = j + dx, i + dy

                    # チェック対象の隣接するマス目が、盤面外に出ていないかチェック
                    # 横のマス目の数(nj)がn以上になっていたら、盤面外。縦のマス目の数(ni)がn以上になっていたら、盤面外。
                    if ni < 0 or ni >= len(grid) or nj < 0 or nj >= len(grid[0]):
                        # 盤面外でも現在地のマスが陸(1)であれば、ansにプラス1する。
                        if grid[i][j] == 1:
                            ans += 1
                        continue

                    # 現在地が陸(1)で、上下左右でそれぞれ水だった場合、ansにプラス1する。
                    if grid[i][j] == 1 and grid[ni][nj] == 0:
                        ans += 1

        return ans

# 他者の解答(DX, DYを使わないで、ifの中で１つ１つ定義して解く方法)
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
    	M, N, p = len(grid), len(grid[0]), 0
        for m in range(M):
            for n in range(N):
                if grid[m][n] == 1:
                    if m == 0 or grid[m-1][n] == 0:
                        p += 1
                    if n == 0 or grid[m][n-1] == 0:
                        p += 1
                    if n == N-1 or grid[m][n+1] == 0:
                        p += 1
                    if m == M-1 or grid[m+1][n] == 0:
                        p += 1
        return p
