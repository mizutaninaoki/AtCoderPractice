# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# DFS+再帰
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            nonlocal curr
            if not node:
                return

            dfs(node.left)  # 左の葉へ移動
            curr.right = node  # node.rightに現在のnodeを入れる
            curr = node # currの位置を今のnodeの位置に移動させる(ポインタで繋がっているansには関係ない)
            curr.left = None # 上のcurr = nodeでcurr.leftに不要なnodeが存在しているので、Noneを入れて左側のnodeを削除する
            dfs(node.right)  # 右の葉へ移動

        ans = curr = TreeNode()
        dfs(root)
        return ans.right # ansの一番最初のnodeにはTreeNode()で初期化した時のnodeがあるため、ans.right以降を返すようにする