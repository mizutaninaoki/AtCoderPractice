# DFS+再帰を使った方法(この問題のreturnはnodeのvalをpreoderの順に配列ansに入れたものを返すらしい。(TrreNodeは返さない))
# preoderはまず左のnodeにできる限り行けるだけ行って、nodeがnodeだったら、１つ前に戻って、右のnodeに行く、というのを繰り返すやり方
# see: https://www.momoyama-usagi.com/entry/info-algo-tree-traverse#__preorder
class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        def dfs(node):
            if not node:
                return

            ans.append(node.val)
            dfs(node.left)
            dfs(node.right)

            return

        ans = []
        dfs(root)
        return ans

# DFS+stackを使った方法


class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:

        #  Ex: root = [1, 2,None, 3,4]
        if not root:
            return []  # __1
        stack, ans = [root], []  # /
        #       2
        while stack:  # / \
            node = stack.pop()  # 3   4
            ans.append(node.val)            #
            #     node     node.left   node.right  stack    ans
            if node.right:  # –––––––––  –––––––––   –––––––––   ––––––  ––––––
                stack.append(node.right)  # [1]     []
            if node. left:  # 1          2         None       [2]     [1]
                # 2          3          4         [4,3]   [1,2]
                stack.append(node.left)
                #       3        None        None       [4]     [1,2,3]
                #       4        None        None       [4]     [1,2,3,4]
        return ans
