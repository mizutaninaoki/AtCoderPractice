# see: https://leetcode.com/problems/missing-number/description/
# 抜けている数列の数を取得するコード
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        for idx, i in enumerate(range(length)):
            if not idx in nums:
                return idx

        return length

# 0~lengthまでの数列の場合、length個×length+1 / 2で一つ大きな値を含んだ時の合計値になる


def missingNumber(self, nums):
    n = len(nums)
    return n * (n+1) / 2 - sum(nums)
