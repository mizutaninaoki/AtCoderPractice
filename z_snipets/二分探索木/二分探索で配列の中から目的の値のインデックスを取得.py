# 二部探索
# see: https://leetcode.com/problems/search-insert-position/description/
class Solution:
    def searchInsert(self, nums, target):
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)/2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                # 真ん中の値(mid)は含めないように+1する
                l = mid+1
            else:
                # 真ん中の値(mid)は含めないように-1する
                r = mid-1
        return l
