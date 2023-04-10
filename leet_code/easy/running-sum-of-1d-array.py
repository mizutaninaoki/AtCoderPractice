# 自分の解答
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        prev = 0
        for i in nums:
            curr = prev + i
            ans.append(curr)
            prev = curr
        return ans

# 他者の解答


def runningSum(self, nums: List[int]) -> List[int]:
	result = []
	total = 0
	for i in range(len(nums)):
		total += nums[i]
		result.append(total)
	return result
