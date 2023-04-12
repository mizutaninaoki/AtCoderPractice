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


# 自分の解答(WA)(DFS+再帰)
# class Solution:
#     def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
#         def dfs(node):
#             if not node:
#                 return

#             if not node.left and not node.right:
#                 ans.append(tmp[-1] + (str(node.val) if tmp[-1][-1] == ">" else "->" + str(node.val)))
#             else:
#                 tmp[-1] += f"->{node.val}"
#             dfs(node.left)
#             dfs(node.right)

#         if not root.left and not root.right:
#             return [str(root.val)]

#         ans = []
#         tmp = [str(root.val)]
#         dfs(root.left)

#         tmp = [str(root.val)]
#         dfs(root.right)
#         return ans
