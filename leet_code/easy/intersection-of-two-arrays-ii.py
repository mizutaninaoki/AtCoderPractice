# 自分の解法(intersectionを使った方法)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        intersection = set(nums1) & set(nums2)
        counter1 = Counter(map(str, nums1))
        counter2 = Counter(map(str, nums2))
        ans = []
        for i in intersection:
            for j in range(min(counter1[str(i)], counter2[str(i)])):
                ans.append(int(i))
        return ans


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
