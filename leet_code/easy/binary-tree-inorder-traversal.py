# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Example1のoutputで[1,3,2]になっているのは、まずroot1から見て、leftには葉がないので次のrootに行って(inorderはleft -> root -> right)、
# rootのvalの１をresにappend。次に2に移動して、2をrootとして見て、leftの3に移動...のように続いていく。
class Solution:
    # recursively
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root:
            self.helper(root.left, res)  # 左の葉へ移動
            res.append(root.val)  # rootのvalを追加
            self.helper(root.right, res)  # 右の葉へ移動


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()  # the last element
            if node:
                if visited:
                    res.append(node.val)
                else:  # preorder: root -> left -> right
                    stack.append((node.right, False))
                    stack.append((node.left, False))
                    stack.append((node, True))
        return res
