# see: https://leetcode.com/problems/maximum-product-of-three-numbers/description/
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        # まず配列をソートし、「2つの最大の負の数と最大の正の数」と「3つの最大の正の数」の積の大きい方が３つの数の積の最大の組み合わせとなる。
        return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])
