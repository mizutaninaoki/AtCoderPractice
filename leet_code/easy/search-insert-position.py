# bisect_leftを使った方法
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        from bisect import bisect_left
        return bisect_left(nums, target)

# 二部探索


class Solution:
    def searchInsert(self, nums, target):
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)/2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
        return l

# 大小比較なシンプルなやり方


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        for i, num in enumerate(nums):
            if num >= target:
                return i

        return len(nums)
