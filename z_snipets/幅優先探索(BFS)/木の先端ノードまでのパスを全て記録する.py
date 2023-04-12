# see: https://leetcode.com/problems/binary-tree-paths/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# bfs + queue
class Solution:
    def binaryTreePaths2(self, root):
        import collections
        if not root:
            return []
        res, queue = [], collections.deque([(root, "")])
        while queue:
            node, ls = queue.popleft()
            # 先端のノードの場合、ここまでのパスをresへ追加する
            if not node.left and not node.right:
                res.append(ls+str(node.val))
            # 左側のノードが存在する場合、キューにこれまでのパスと今のノードの値(node.val)をくっつけて、追加する
            if node.left:
                queue.append((node.left, ls+str(node.val)+"->"))
            # 右側のノードが存在する場合、キューにこれまでのパスと今のノードの値(node.val)をくっつけて、追加する
            if node.right:
                queue.append((node.right, ls+str(node.val)+"->"))
        return res
