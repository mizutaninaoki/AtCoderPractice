# see: https://leetcode.com/problems/path-sum/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# DNS + stack
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        # 現時点の深さでの値の合計(sum)は別で持っておく。でないと一番深い葉まで到達して、
        # TargetSumと同じで無い場合、上の葉に戻る際、上の葉までの合計値がわからなくなってしまうから。
        stack = [(root, root.val)]
        while stack:
            curr, curr_sum = stack.pop()
            # 子を持たないノード(リーフ)まで到達した時の合計がtargetSumと同じで無いといけない（子ノードを持たないノードに辿り着く前にtargetSumと同じ合計になってもTrueにはならない）
            if not curr.left and not curr.right and curr_sum == targetSum:
                return True
            if curr.right:
                stack.append((curr.right, curr_sum+curr.right.val))
            if curr.left:
                stack.append((curr.left, curr_sum+curr.left.val))
        return False


# DNS + 再帰
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        res = []
        self.dfs(root, targetSum, res)
        return any(res)

    def dfs(self, root, targetSum, res):
        if root:
            if not root.left and not root.right and root.val == targetSum:
                res.append(True)
            if root.left:
                self.dfs(root.left, targetSum-root.val, res)
            if root.right:
                self.dfs(root.right, targetSum-root.val, res)
