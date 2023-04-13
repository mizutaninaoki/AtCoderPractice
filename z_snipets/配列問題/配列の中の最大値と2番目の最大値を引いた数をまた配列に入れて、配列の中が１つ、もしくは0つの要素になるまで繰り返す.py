# see: https://leetcode.com/problems/last-stone-weight/description/
# 自分の解答
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # insort_leftでソート順を考慮して、値をリストに挿入してくれる
        from bisect import insort_left
        stones.sort()
        ans = 0

        # stonesの中身の値が１つ以下になるまでループさせる
        while len(stones) > 1:
            max_stone = stones.pop()
            second_max_stone = stones.pop()
            diff = max_stone - second_max_stone
            if diff:
                insort_left(stones, diff)

        # 中身が残っていたら、その中身の値を返し、残っていなかったら0を返す
        return stones[0] if stones else 0
