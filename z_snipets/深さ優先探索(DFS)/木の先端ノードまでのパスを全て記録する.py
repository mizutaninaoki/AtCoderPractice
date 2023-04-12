# see: https://leetcode.com/problems/binary-tree-paths/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 他者の解答(DFS+再帰)
class Solution:
    def binaryTreePaths(self, root):
        def dfs(root, ls, res):
            # 先端のノードの場合、ここまでのパスをresへ追加する
            if not root.left and not root.right:
                res.append(ls+str(root.val))
            # 左側のノードが存在する場合、ここまでのパスと今のノードの値(node.val)をくっつけて、再帰する
            if root.left:
                dfs(root.left, ls+str(root.val)+"->", res)
            # 右側のノードが存在する場合、ここまでのパスと今のノードの値(node.val)をくっつけて、再帰する
            if root.right:
                dfs(root.right, ls+str(root.val)+"->", res)

        if not root:
            return []
        res = []
        dfs(root, "", res)
        return res
