# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 自分の解答(DFS+再帰)
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        from collections import defaultdict
        def dfs(node, depth):
            nonlocal d1, d2
            if not node:
                return

            # 辞書1にnode.valの合計値をdepth毎に集計
            d1[depth] += node.val
            # 辞書2にノードの数の合計値をdepth毎に集計
            d2[depth] += 1
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)

        ans = []
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        dfs(root, 0)

        # それぞれの深さ毎に平均を出して、ansへ追加
        for i, j in zip(d1, d2):
            ans.append(d1[i] / d2[j])
        return ans
        