# see: https://leetcode.com/problems/invert-binary-tree/
# DFS(stackを使う(ただの配列にpop()で取り出していく。pop()は最後のインデックスの値を取り出す。つまり先入れ先出しでstack。))
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            # 先入れ先出し(stack.extend([])した一番新しい値を配列から削除して取り出す)
            node = stack.pop()
            if node:
                # node.left = node.right
                # node.right = node.left
                # 上のように書くと、２行目でnode.rightにnode.leftを代入するときに、すでにnode.leftの値が１行目で変わってしまっているため、下記のように書かなくてはいけない。
                # (それか一旦別の変数にnode.leftの値を一時的に保持しておくか)
                node.left, node.right = node.right, node.left
                # appendは１つの要素しか追加できない。extendは配列で二重配列にならずに値だけ複数追加できる。
                stack.extend([node.right, node.left])
        return root