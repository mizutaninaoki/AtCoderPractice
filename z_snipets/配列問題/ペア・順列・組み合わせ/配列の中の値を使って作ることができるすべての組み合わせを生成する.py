# see: https://leetcode.com/problems/subsets/description/
# 自分の解答(combinationsを使う)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations
        ans = []
        for i in range(len(nums)+1):
            # 0個〜3個までの全通りの組み合わせをansに追加する。(combinationの数の指定を0にすると、空の配列が返ってくる)
            ans.extend(list(combinations(nums, i)))
        return ans


# resultの配列にnumsの値を1つずつ足して、それのリストをまたresultに追加していく解法
class Solution(object):
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = [[]]
        for num in nums:
            result += [i + [num] for i in result]
        return result
