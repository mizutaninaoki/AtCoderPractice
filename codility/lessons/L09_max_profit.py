# 100%
def solution(A):
    if len(A) == 0:
        return 0
    min_price = A[0]
    max_profit = 0
    for i in A[1:]:
        min_price = min(min_price, i)
        max_profit = max(max_profit, i - min_price)
    return max_profit
