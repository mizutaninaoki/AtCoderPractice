# see: https://leetcode.com/problems/binary-tree-postorder-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# ---------------------------------
# postorderはleft -> right -> root
# 参考: https://engineer.yeele.net/algorithm/data-structure/binary-tree-traversal/
#      https://leetcode.com/problems/binary-tree-inorder-traversal/solutions/283746/all-dfs-traversals-preorder-inorder-postorder-in-python-in-1-line/?orderBy=most_votes&languageTags=python
#      https://leetcode.com/problems/binary-tree-inorder-traversal/solutions/31381/python-recursive-and-iterative-solutions/
# ---------------------------------
class Solution:
    # recursively
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root:
            self.helper(root.left, res)  # 左の葉へ移動
            self.helper(root.right, res)  # 右の葉へ移動
            res.append(root.val)  # rootのvalを追加

# メソッド名をdfsに変更したバージョン(defはclass Solutionの中に移動)


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
