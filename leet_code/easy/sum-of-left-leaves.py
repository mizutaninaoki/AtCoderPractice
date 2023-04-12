# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 自分の解答(DFS+再帰)
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, is_left):
            nonlocal ans
            if not node:
                return

            # 左側のノード、かつ、子を持たないノード(リーフ)の場合、node.valをansに足す
            if is_left and not node.left and not node.right:
                ans += node.val
            dfs(node.left, True)  # 左のノードの時だけ、is_leftをTrueにする
            dfs(node.right, False)

        ans = 0
        # 初回のis_leftはFalseにする
        dfs(root, False)
        return ans


# 他者の解答(再帰)
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # does this node have a left child which is a leaf?
        if root.left and not root.left.left and not root.left.right:
		# gotcha
            return root.left.val + self.sumOfLeftLeaves(root.right)

        # no it does not have a left child or it's not a leaf
        else:
		# bummer
            return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
