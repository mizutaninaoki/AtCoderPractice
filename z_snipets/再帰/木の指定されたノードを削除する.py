# see: https://leetcode.com/problems/delete-node-in-a-bst/description/
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