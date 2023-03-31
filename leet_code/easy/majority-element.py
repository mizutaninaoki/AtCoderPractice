class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter

        counter = Counter(nums)
        # 最大のvalueのキーを返す
        return max(counter, key=counter.get)
