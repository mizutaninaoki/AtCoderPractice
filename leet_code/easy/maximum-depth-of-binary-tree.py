# -------------------
# 自分のコード(WA)
# -------------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def __init__(self):
#         self.left_depth = 1
#         self.right_depth = 1

#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         self.dfs(root.left, root.right)
#         return max(self.left_depth, self.right_depth)


#     def dfs(self, l, r):
#         if l:
#             self.left_depth += 1
#             self.dfs(l.left, l.right)
#         if r:
#             self.right_depth += 1
#             self.dfs(r.left, r.right)

# DFS
class Solution(object):
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # rootから見て左と右の葉をそれぞれDFSしていって、一番深い葉まで到達して、rootがNoneだったら、そこから再帰でプラス１ずつしていく
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


class Solution(object):
    # level by level
    from collections import deque

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        deque, depth = deque(), 0
        if root:
            deque.append(root)
        while deque:
            size = len(deque)
            for _ in range(size):
                node = deque.popleft()
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            depth += 1
        return depth


# BFS + deque
class Solution(object):
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        from collections import deque
        queue = deque([(root, 1)])
        while queue:
            curr, val = queue.popleft()
            if not curr.left and not curr.right and not queue:
                return val
            if curr.left:
                queue.append((curr.left, val+1))
            if curr.right:
                queue.append((curr.right, val+1))
