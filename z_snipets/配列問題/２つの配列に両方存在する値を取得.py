# see: https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Counterを使った簡潔なコード
class Solution(object):
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        counts = Counter(nums1)
        res = []

        for num in nums2:
            # counterを使って求めた各数の個数分、共通する数をresの配列に追加していく
            if counts[num] > 0:
                # 数字を配列に+=で追加する場合、お尻に「,(コンマ)」をつけないとエラーになる（「res += num」でお尻にコンマつけないとエラー）
                res += num,
                counts[num] -= 1

        return res