# see: https://leetcode.com/problems/first-bad-version/description/
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n - 1
        # 二分探索
        # 最終的にleftに最初にisBadVersion(mid)でTrueが返ってくるインデックス+1、つまりnの数字が返ってくる。
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid) == False:
                left = mid + 1
            elif isBadVersion(mid) == True:
                right = mid - 1
        return left