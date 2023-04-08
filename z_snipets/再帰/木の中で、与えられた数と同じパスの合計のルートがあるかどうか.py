# see: https://leetcode.com/problems/path-sum/description/
# 再帰のみ


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        # 子を持たないノード(リーフ)まで到達した時の合計がtargetSumと同じで無いといけない（子ノードを持たないノードに辿り着く前にtargetSumと同じ合計になってもTrueにはならない）
        # targetSumと現在のノードまでの合計の差が0であれば、その時点までのパスの合計がtargetSumと同じだということ。
        if not root.left and not root.right and root.val == targetSum:
            return True
        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)
