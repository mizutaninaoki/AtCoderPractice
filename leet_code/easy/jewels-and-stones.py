# 自分の解答
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        from collections import Counter
        counter = Counter(stones)

        ans = 0
        for i in jewels:
            ans += counter[i]
        return ans
