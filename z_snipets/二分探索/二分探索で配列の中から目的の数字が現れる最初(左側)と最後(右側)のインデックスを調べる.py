# see: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
# 自分の解答(bisect使用)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        from bisect import bisect_left, bisect_right
        left_idx = bisect_left(nums, target)
        right_idx = bisect_right(nums, target)

        if nums.count(target) == 0:
            return [-1, -1]
        else:
            return [left_idx, right_idx - 1]

# 二分探索を自分で定義する解法


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # targetの数字の中で一番左側に存在する位置を探る二分探索用メソッド
        def binarySearchLeft(A, x):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = (left + right) / 2
                if x > A[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        # targetの数字の中で一番右側に存在する位置を探る二分探索用メソッド
        def binarySearchRight(A, x):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = (left + right) / 2
                if x >= A[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        # left <= rightが正しければ(targetの数字がない、もしくは、targetの数字が１つしかない以外)
        # binarySearchLeft、binarySearchRight、共にtargetの数字がない場合、leftとraightは同じ数字になっているはず
        left, right = binarySearchLeft(
            nums, target), binarySearchRight(nums, target)
        return (left, right) if left <= right else [-1, -1]
