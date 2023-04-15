# 自分の解答(TLE)
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         def dfs(down, right):
#             # 最終地点の座標は(m-1, n-1)
#             if down == m - 1 and right == n - 1:
#                 nonlocal ans
#                 ans += 1
#                 return
            
#             # 下に行ける場合は下に進む
#             if down < m:
#                 dfs(down+1, right)
#             # 右に行ける場合は右に進む
#             if right < n:
#                 dfs(down, right+1)

#         ans = 0
#         down = 0
#         right = 0
#         dfs(down, right)
#         return ans
    
# 他者の回答1(DP)
# O(m*n) space
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m、もしくはnが0であればreturn 0する。
        if not m or not n:
            return 0
        
        # マス目分のdpの配列を作る
        # 右か下しか進めない場合(戻ることができない場合)、一番上の行と一番左の列に行く方法はどちらも１通りしかない(「下、下」とか「右、右、右、右、右、右、右」とか)。
        # なので、初期値は全て1にしておく。(一番上の行と一番左の列以外はループ途中で書き換えられる。)
        dp = [[1 for _ in range(n)] for _ in range(m)]
        # スタート地点は(0, 0)、なので移動できるのは、下に1,2、右に1,2,3,4,5,6であり、(2, 6)がゴール地点になる。
        for i in range(1, m):
            for j in range(1, n):
                # 一つ前の地点までに辿り着くことができるルートの数をそれぞれ、上(dp[i-1][j])と左(dp[i][j-1])の値を足し合わせて、現在地まで辿り着けるルートの数を算出する。
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # ゴール地点に入っている値が、ここまでくることができるルートの数になる
        return dp[-1][-1]

# ちなみに最終的にdpには以下のような値が入り、そのマスまでのルートの数がそれぞれ格納されている。
# [[1, 1, 1, 1, 1, 1, 1],
# [1, 2, 3, 4, 5, 6, 7],
# [1, 3, 6, 10, 15, 21, 28]]

# 他者の回答2(DP)
# O(n) space
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if not m or not n:
            return 0
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
        return cur[-1]