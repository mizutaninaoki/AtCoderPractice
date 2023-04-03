# see: https://leetcode.com/problems/invert-binary-tree/
# 再帰１
class Solution:
    # recursively
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            print(f"{root.val}: ", root)
            root.right, root.left = self.invertTree(
                root.left), self.invertTree(root.right)
            return root
# 再帰２


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        self.invertTree(root.left)
        self.invertTree(root.right)
        # 先端のノードの時、root.rightとroot.leftにはどちらもNoneになっているため、入れ替えても何もかわらない。
        # 先端でないノードの場合、そのノードより先の部分ツリーをroot.rightとroot.leftを入れ替えることにより、左右対称に入れ替えることになる。
        root.left, root.right = root.right, root.left
        return root