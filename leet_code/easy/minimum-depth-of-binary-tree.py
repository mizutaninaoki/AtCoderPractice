# DFS+再帰
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return self.minDepth(root.left or root.right) + 1


# DFS+stack
class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        # res can be set as max_int
        res, stack = 9999, [(root, 1)]
        while stack:
            node, level = stack.pop()
            if node and not node.left and not node.right:
                res = min(res, level)
            if node:
                stack.append((node.left, level+1))
                stack.append((node.right, level+1))
        return res


# BFS
class Solution:
    def minDepth(self, root):
        import collections
        if not root:
            return 0
        queue = collections.deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if node:
                if not node.left and not node.right:
                    return level
                else:
                    queue.append((node.left, level+1))
                    queue.append((node.right, level+1))
