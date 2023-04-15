# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 自分の解答(DFS)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(node, depth):
            if not node:
                return

            # ansに深さ分(depth)のリストが存在しない場合は空のリストを入れておいて、ans[depth].append(node.val)でエラーにならないようにする。
            if len(ans)-1 < depth:
                ans.append([])
            # 現在の深さ(depth)に対応するansの中のリストに、node.valを追加する
            ans[depth].append(node.val)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)

        ans = []
        dfs(root, 0)
        return ans

# 他者の解答(whileを使った解答)


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        next_queue = []
        level = []
        result = []

        while queue:
            for root in queue:
                level.append(root.val)
                if root.left:
                    next_queue.append(root.left)
                if root.right:
                    next_queue.append(root.right)
            result.append(level)
            level = []
            queue = next_queue
            next_queue = []

        return result
