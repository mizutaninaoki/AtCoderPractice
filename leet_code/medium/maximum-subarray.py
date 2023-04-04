class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -inf
        tmp_sum = 0
        for i in nums:
            tmp_sum = max(i, tmp_sum + i)
            ans = max(ans, tmp_sum)
        return ans
