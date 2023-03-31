class Solution(object):
    # DFSで一番深い葉まで探索して、木の一番深い深さを取得
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # rootから見て左と右の葉をそれぞれDFSしていって、一番深い葉まで到達して、rootがNoneだったら、そこから再帰でプラス１ずつしていく
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
