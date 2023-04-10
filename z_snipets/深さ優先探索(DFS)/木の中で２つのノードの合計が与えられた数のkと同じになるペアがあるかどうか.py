# see: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
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
