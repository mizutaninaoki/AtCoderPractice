# setの引き算を使う方法
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        include_s = set([i for i in range(1, len(nums)+1)])
        return list(include_s - s)  # 1~len(nums)まででnumsに含まれない数を集合の引き算で算出する


# すでにリストnumsに存在する値は全て負の値に変換するやり方
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            a = abs(n) - 1
            if nums[a] > 0:
                nums[a] *= -1
        return [i+1 for i in range(len(nums)) if nums[i] > 0]
