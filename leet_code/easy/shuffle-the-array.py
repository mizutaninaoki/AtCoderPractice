
# see: https://leetcode.com/problems/shuffle-the-array/description/
# 自分の解答(左右に分けて、ansに追加していくだけ)
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left = nums[:n+1]
        right = nums[n:]

        ans = []
        for l, r in zip(left, right):
            ans.extend([l, r])
        return ans
