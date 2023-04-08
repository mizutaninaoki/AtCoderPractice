# see: https://leetcode.com/problems/merge-two-binary-trees/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 再帰で解く
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # root1かroot2の両方のnodeが存在すれば、両方のvalを足し合わせたvalのnodeを返す。
        # どちらか片方しか存在しない場合は存在しているnodeだけ返す。
        # どちらも存在しない場合は、何も返さない(Noneを返す)
        if root1 and root2:
            root = TreeNode(root1.val + root2.val)
            root.left = self.mergeTrees(root1.left, root2.left)
            root.right = self.mergeTrees(root1.right, root2.right)
            return root
        else:
            return root1 or root2
