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
