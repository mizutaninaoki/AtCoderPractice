# 自分の解答
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        from collections import defaultdict
        d = defaultdict(list)
        for i in range(len(nums)):
            if nums[i] in d:
                # 辞書の中にnums[i]の数字がこれまでの中で登場したインデックスが全部入っているため、ループで回して、
                # 条件(abs(j - i) <= k)に合致していないかチェックする。
                for j in d[nums[i]]:
                    if abs(j - i) <= k:
                        return True

            # numsの値をキーにして、値ごとにnumsのインデックスをvalueの配列の中に追加する
            d[nums[i]].append(i)
        return False


# 他者の解答
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False
