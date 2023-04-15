# see: https://leetcode.com/problems/permutations/description/
# 自分の解答(itertools.permutationsを使用)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        return permutations(nums, len(nums))

# DFS+再帰


class Solution:
    def permute(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        # numsがなくなったら、それまでのpathに入っている組み合わせをresに追加
        if not nums:
            res.append(path)
            return  # returnしなくてもnumsは空の配列のため、正しく動作するが、一応returnしている
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)

# dfsを通過する経過(print(nums, path))
# [1, 2, 3] []
# [2, 3] [1]
# [3] [1, 2]
# [] [1, 2, 3]
# [2] [1, 3] <- numsが[2,3]の時に、rangeの中でiが1(range内にて2回目のループ)の時に呼ばれたdfs()
# [] [1, 3, 2]
# [1, 3] [2] <- numsが[1,2,3]の時に、rangeの中でiが1(range内にて2回目のループ)の時に呼ばれたdfs()
# [3] [2, 1]
# [] [2, 1, 3]
# [1] [2, 3]
# [] [2, 3, 1]
# [1, 2] [3]
# [2] [3, 1]
# [] [3, 1, 2]
# [1] [3, 2]
# [] [3, 2, 1]
