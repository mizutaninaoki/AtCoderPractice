# 自分の解答
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            # 現在のインデックスよりも後に同じ数字が出現する回数 == ペアの数
            ans += nums[i+1:].count(nums[i])
        return ans
