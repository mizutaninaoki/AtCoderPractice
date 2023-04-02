from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')

        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit


# 以下の二重ループで回すと、TLEになる。
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max_price = 0
#         for i in range(len(prices)):
#             for j in range(i, len(prices)):
#                 max_price = max(max_price, prices[j] - prices[i])
#         return max_price
