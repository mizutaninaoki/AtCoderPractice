# 平衡２分探索木」の１つである「AVL 木」の説明
# https://daeudaeu.com/avl_tree/
# 「AVL 木」のように、「木の高さを自動的にできるだけ小さく維持しようとする２分探索木」を平衡２分探索木と言います。

# see: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/solutions/2406277/python-easily-understood-faster-than-86-less-than-83-recursion/
# 以下は、昇順でソートされた配列の高さをできるだけ高さが小さい（どのノードの左右部分木の高さの差も１以下）木である平衡２分探索木にするためのコード
# 平衡２分探索木 -> 「左の子ノードの値 ≦ ノードの値 ≦ 右の子ノードの値」の関係性に則って、構成されている
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
           # 最初からnumsがNone。もしくは二分探索を繰り返してnumsに値がなくなったらNoneを返して再帰をのぼっていく。
           if not nums:
                return None

            mid = len(nums) // 2
            # 二分探索で中央の値(mid)にてTreeNodeを初期化
            root = TreeNode(nums[mid])
            # 配列にて真ん中の値(mid)は含めたくないため、+1はしない。
            root.left = self.sortedArrayToBST(nums[:mid])
            root.right = self.sortedArrayToBST(nums[mid+1:])

            return root
