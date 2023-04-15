# see: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 他者の解答(再帰を使っている。よくわかってない。。。)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            # in-order traversalのルートノードのインデックスを探す
            index = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[index])
            print(root)

            # 0番目のインデックスからルートインデックスまでの左サブツリーをin-order traversalで再帰的に生成する。
            root.left = self.buildTree(preorder, inorder[:index])

            # ルートインデックスの次から最後のインデックスまで、右サブツリーを再帰的に生成する。
            root.right = self.buildTree(preorder, inorder[index+1:])
            return root
