# see: https://leetcode.com/problems/invert-binary-tree/
# BFS(dequeを使う!!!)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        import collections
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
