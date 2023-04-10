# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 自分の解答(DFS+再帰)
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return

            nonlocal vals
            # node.valの値がlow以上、high以下であればvalsに追加
            if low <= node.val <= high:
                vals.append(node.val)
            dfs(node.left)
            dfs(node.right)

        vals = []
        dfs(root)
        return sum(vals)


# 再帰だけ使った方法
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root == None:
            return 0
        if root.val > R:
            return self.rangeSumBST(root.left, L, R)
        if root.val < L:
            return self.rangeSumBST(root.right, L, R)
        return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
