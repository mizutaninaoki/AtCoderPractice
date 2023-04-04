# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

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


class Solution(object):
    def isBalanced(self, root):
        stack, node, last, depths = [], root, None, {}
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or last == node.right:
                    node = stack.pop()
                    left, right = depths.get(
                        node.left, 0), depths.get(node.right, 0)
                    if abs(left - right) > 1:
                        return False
                    depths[node] = 1 + max(left, right)
                    last = node
                    node = None
                else:
                    node = node.right
        return True
