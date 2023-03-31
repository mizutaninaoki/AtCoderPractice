# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # rootがなかったら、nodeが１つもないので、True
        if not root:
            return True
        # rootから見て、左のnodeと右のnodeをDFSでシンメトリーになっているか比較
        return self.dfs(root.left, root.right)

    def dfs(self, l, r):
        # １、シンメトリーに対応する左右のnodeの値を確認
        # ２、再帰でまた、シンメトリー同士（「左の葉と右の葉」、「右の葉と左の葉」）の値が同じかチェックしていく（深さ優先探索）
        # ３、lとrでどちらかがNoneだったら、lとrどちらもNoneでシンメトリーになっているかチェックした値を返す
        if l and r:
            return l.val == r.val and self.dfs(l.left, r.right) and self.dfs(l.right, r.left)
        return l == r


# stackを使った解答
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        # 初期値にはrootの左右の葉を入れておく
        stack = [(root.left, root.right)]
        while stack:
            l, r = stack.pop()
            # lとr、どちらもNoneであればcontinue（それでstackなくなってwhileから抜けるかな）
            if not l and not r:
                continue
            # lとr、どちらかがNoneであれば、lとrどちらもNoneであるか比較して、どちらか一方に値が存在すればシンメトリーではないため、Falseを返す
            if not l or not r or (l.val != r.val):
                return False
            # 上のif文を通ってきた場合、この時点ではシンメトリーなので、今時点よりも１つ深い葉をstackに追加していく。
            stack.append((l.left, r.right))
            stack.append((l.right, r.left))
        return True
