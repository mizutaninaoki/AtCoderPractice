# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # recursively
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root, res):
            if root:
                dfs(root.left, res)  # 左の葉へ移動
                dfs(root.right, res)  # 右の葉へ移動
                res.append(root.val)  # rootのvalを追加
        res = []
        dfs(root, res)
        return res
