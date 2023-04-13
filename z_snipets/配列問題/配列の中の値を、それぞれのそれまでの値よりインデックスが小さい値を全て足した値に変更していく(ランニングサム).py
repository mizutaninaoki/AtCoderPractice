# see: https://leetcode.com/problems/running-sum-of-1d-array/description/
def runningSum(self, nums: List[int]) -> List[int]:
	result = []
	total = 0
	for i in range(len(nums)):
		total += nums[i]
		result.append(total)
	return result
