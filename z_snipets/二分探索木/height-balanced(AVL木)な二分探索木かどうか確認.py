# see: https://leetcode.com/problems/balanced-binary-tree/
# 再帰を使った方法
# height-balanced == どのノードの左右部分木の高さの差も１以下の二分探索木(深さが１だけ違うのであればOK)
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if root is None:
                return 0
            left = check(root.left)
            right = check(root.right)
            # leftかrightに-1が入っていたら、すでに深さが１以上の部分が存在しているということだから、引き続き-1を返して、最終的にFalseを返す
            # 絶対誤差が2以上の時はheight-balancedではないため、　-1にする。
            # この再帰のイメージとしては、再帰でまずは一番深いnodeまで探索して、そこから１つ上に上がるにつれて、1ずつ足していっているイメージ。
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return check(root) != -1
