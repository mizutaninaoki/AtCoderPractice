# see: https://leetcode.com/problems/range-sum-of-bst/description/
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
