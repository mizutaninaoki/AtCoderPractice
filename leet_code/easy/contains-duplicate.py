# 配列の中に重複がないかチェックするコード
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        for i in Counter(nums).values():
            if i >= 2:
                return True
        return False

# setを使うやり方
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums))!=len(nums)