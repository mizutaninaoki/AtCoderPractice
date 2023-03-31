# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
            # 最初からnumsがNone。もしくは二分探索を繰り返してnumsに値がなくなったらNoneを返して再帰をのぼっていく。
            if not nums:
                return None

            mid = len(nums) // 2
            # 二分探索で中央の値(mid)にてTreeNodeを初期化
            root = TreeNode(nums[mid])
            # 配列にて真ん中の値(mid)は含めたくないため、+1はしない。
            root.left = self.sortedArrayToBST(nums[:mid])
            root.right = self.sortedArrayToBST(nums[mid+1:])

            return root

# もう一つの解答（以下URLの図がわかりやすい）
# see: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/solutions/2406277/python-easily-understood-faster-than-86-less-than-83-recursion/


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        total_nums = len(nums)
        if not total_nums:
            return None

        mid_node = total_nums // 2
        return TreeNode(
            nums[mid_node],
            self.sortedArrayToBST(nums[:mid_node]), self.sortedArrayToBST(
                nums[mid_node + 1:])
        )
