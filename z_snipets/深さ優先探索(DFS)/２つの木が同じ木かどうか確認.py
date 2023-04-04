# see: https://leetcode.com/problems/same-tree/
# DFS(stack使用を使った解き方)
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        from collections import deque
        p_que = deque([p])
        q_que = deque([q])

        while p_que and q_que:
            p_node = p_que.popleft()
            q_node = q_que.popleft()
            # どちらのノードもNoneの場合はcontinue
            if not p_node and not q_node:
                continue
            # どちらかのノードがNoneであればFalseを返す
            if not p_node or not q_node:
                return False
            # ノードのvalが同じではなければ、ツリー構造が違うためFalseを返す
            if p_node.val != q_node.val:
                return False
            p_que.extend([p_node.left, p_node.right])
            q_que.extend([q_node.left, q_node.right])
        return True

# 再帰を使った解き方


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        else:
            return p.val == q.val and self.recursive(p.left, q.left) and self.recursive(p.right, q.right)
