# dpで解く方法
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0

        dp = [0] * len(cost)
        dp[0] = cost[0]  # 一段目へ来るのはスタート地点（costの配列外）から一歩歩いてくるパターンしかないため、cost[0]がdp[0]になる
        # 二段目へ来るのはスタート地点（costの配列外）から一段飛ばしで歩いてくるパターンしかないため、cost[0]がdp[0]になる
        dp[1] = cost[1]

        # 例えば、インデックス２の最小値は、dp[2] = cost[2] + min(dp[0], dp[1])
        # つまり、dp[i]は「cost[i] + min(dp[i-2], dp[i-1]) 」となります。(現在の階段でのコストに、前の階段のminを足したもの)
        # dp[0]とdp[1]はすでに知っているので、2からスタート
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])

        # この時点で２番目のexampleだったら、dpの中身は以下のようになっている
        # [1, 100, 2, 3, 3, 103, 4, 5, 104, 6]

        # 最後は、最後の階段から一歩歩くパターンと、最後から２番目の階段から一段飛ばしで歩いてくる可能性がある。
        # そのため、dp[-1]とdp[-2]にメモされている中で、小さい方が答えの最小値となる。
        return min(dp[-1], dp[-2])
