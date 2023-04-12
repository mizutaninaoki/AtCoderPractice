# 自分の解答
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            tmp = 0
            for j in nums:
                if j < i:
                    tmp += 1
            ans.append(tmp)
        return ans
