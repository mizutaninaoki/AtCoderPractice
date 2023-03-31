# ------------------------------------------------
# 木構造が左右対称かどうかDFSを使って確認している
# 問題：https://leetcode.com/problems/symmetric-tree/
# ------------------------------------------------
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # rootがなかったら、nodeが１つもないので、True
        if not root:
            return True
        # rootから見て、左のnodeと右のnodeをDFSでシンメトリーになっているか比較
        return self.dfs(root.left, root.right)

    def dfs(self, l, r):
        # １、シンメトリーに対応する左右のnodeの値を確認
        # ２、再帰でまた、シンメトリー同士（「左の葉と右の葉」、「右の葉と左の葉」）の値が同じかチェックしていく（深さ優先探索）
        # ３、lとrでどちらかがNoneだったら、lとrどちらもNoneでシンメトリーになっているかチェックした値を返す
        if l and r:
            return l.val == r.val and self.dfs(l.left, r.right) and self.dfs(l.right, r.left)
        return l == r
