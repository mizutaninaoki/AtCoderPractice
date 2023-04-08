# see: https://leetcode.com/problems/path-sum/description/
# BFS with queue
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        # 一番上のノードから順番に浅いノードを見ていくため、targetSumとルートノードが持つ値の差を保持しておいて、差が0になったら、合計値がtargetSumと同じになったということになる。
        queue = [(root, targetSum-root.val)]
        while queue:
            curr, val = queue.pop(0)
            # 子を持たないノード(リーフ)まで到達した時の合計がtargetSumと同じで無いといけない（子ノードを持たないノードに辿り着く前にtargetSumと同じ合計になってもTrueにはならない）
            if not curr.left and not curr.right and val == 0:
                return True
            if curr.left:
                queue.append((curr.left, val-curr.left.val))
            if curr.right:
                queue.append((curr.right, val-curr.right.val))
        return False
