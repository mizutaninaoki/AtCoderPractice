# see: https://leetcode.com/problems/search-in-a-binary-search-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 自分の解答(DFS+再帰)
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node):
            nonlocal ans
            if not node:
                return

            # node.valと同じvalがあれば、ansへ保持させておく
            if node.val == val:
                ans = node
            dfs(node.left)
            dfs(node.right)

        ans = None
        dfs(root)
        return ans
