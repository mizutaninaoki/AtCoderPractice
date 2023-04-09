# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 自分の解答(WE)
# class Solution:
#     def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
#         if not root:
#             return root
        
#         stack = []
#         parents = root

#         while stack:
#             node = stack.pop()

#             if node.left and node.left.val == key:
#                 if node.left.left:
#                     tmp_node = node.left.left
#                     node.left = node.left.right
#                     node.left.left = tmp_node
#                 elif node.left.right:
#                     node.right = node.left.right
#             elif node.right and node.right.val == key:
#                 if node.right.right:
#                     tmp_node = node.right.right
#                     node.right = node.right.right
#                     node.right.right = tmp_node
#                 elif node.right.left:
#                     node.right = node.right.left          
         
#             stack.append(node.right)
#             stack.append(node.left)
#         return root


# 他者の解答(再帰)
class Solution(object):
     def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None
        
        if root.val == key:
            if root.left:
                # 左の部分木の一番右の葉を探す
                left_right_most = root.left
                while left_right_most.right:
                    left_right_most = left_right_most.right
                # その葉の右側に右の子をつける
                left_right_most.right = root.right
                # ルートではなく、左の子を返す。
                return root.left
            else:
                return root.right
        # If left or right child got deleted, the returned root is the child of the deleted node.
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
            
        return root