class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx1, i in enumerate(nums):
            for idx2, j in enumerate(nums[idx1+1:]):
                if i + j == target:
                    return [idx1, idx2 + idx1+1]
