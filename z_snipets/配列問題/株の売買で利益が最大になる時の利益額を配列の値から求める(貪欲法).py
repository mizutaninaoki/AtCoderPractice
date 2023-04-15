# see: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
# 貪欲法を使った解法
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # pricesが空のリスト、もしくは値が1つしかなかったら、0を返す
        if not prices or len(prices) == 1:
            return 0

        profit = 0
        # 前の値より現在の値の方が大きかったら、現在の値と前の値の差をprofitに足していく(貪欲法)
        # 前の値より現在の値が大きく、次の値がもっと大きい値でも、今回売ってしまうと同時に、再度株を買ってしまったら、結局最大の利益(差)は同じになるから、貪欲法でいける。
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]

        return profit
