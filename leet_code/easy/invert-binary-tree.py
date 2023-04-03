# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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

# BFS(dequeを使う!!!)


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = collections.deque([root])
        while queue:
            # ルートのノードから探索していき、１つ下のノードをテレコにしてから、テレコにしたノードをスタックに追加していく。
            # 一番先端まで到達した時は、nodeはNoneなので、スタックに追加された先端のノードはただ削除されるだけ
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root


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
        # left, rightにはポインタが格納されているから、nodeという変数で上で処理しているが、ちゃんとrootの中もシンメトリーに変更されている
        return root
