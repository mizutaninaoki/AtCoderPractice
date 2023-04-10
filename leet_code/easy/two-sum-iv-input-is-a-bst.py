# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 自分の解答(DFS+再帰)
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def dfs(node):
            # def dfsの外の変数の値をdef dfs内で変更したいときはnonlocal宣言をしないといけない！
            nonlocal vals, ans
            if not node:
                return

            # このノードまでに保管したvalsの中に、今回の値(i)と足してkになるペアがあるかどうかチェック
            for i in vals:
                if node.val + i == k:
                    ans = True
                    break
            # 次のノードの値と足してkになるペアがあるかどうかチェックするためにvalsに追加しておく。
            vals.add(node.val)
            dfs(node.left)
            dfs(node.right)

        ans = False
        vals = set()
        dfs(root)
        return ans


# DFS+stackを使った解答
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        stack, seen = [root], set()

        while stack:
            curr = stack.pop()
            # If we've seen k - curr.val,
            # we have k - curr.val + curr.val = k
            if k - curr.val in seen:
                return True
            seen.add(curr.val)

            # Visit children
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)

        return False
