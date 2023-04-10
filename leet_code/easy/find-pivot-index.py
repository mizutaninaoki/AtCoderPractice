# 自分の解答
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = 0
        curr_idx = 0

        # 現在のインデックス(curr_idx)が与えられた配列numsの最後までスライドさせても、leftとrightが同じ値にならなければ、ループを抜ける。
        while curr_idx <= len(nums) - 1:
            left = sum(nums[:curr_idx])
            right = sum(nums[curr_idx+1:])
            # leftとrightが同じ値かどうかチェック
            if left == right:
                return curr_idx

            curr_idx += 1

        return -1


# leftSumは最初0。rightSumには配列すべての合計値を入れておいて、左から１つずつ、値を取り出して引いていって、leftとrightが同じ合計値になるかどうかチェック。
class Solution(object):
    def pivotIndex(self, nums):
        # Initialize leftSum & rightSum to store the sum of all the numbers strictly to the index's left & right respectively...
        leftSum, rightSum = 0, sum(nums)
        # Traverse elements through the loop...
        for idx, ele in enumerate(nums):
            rightSum -= ele
            # If the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right...
            if leftSum == rightSum:
                return idx      # Return the pivot index...
            leftSum += ele
        # If there is no index that satisfies the conditions in the problem statement...
        return -1
