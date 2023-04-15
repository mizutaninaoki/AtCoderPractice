# see: https://leetcode.com/problems/sort-colors/description/
# 自分の解答(Counter()を使う)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        from collections import Counter
        c = Counter(nums)
        nums[:] = ([0] * c[0]) + ([1] * c[1]) + ([2] * c[2])


# 0=赤
# 1=白
# 2=青
# 配列を赤、白、未分類、青の 4 つのグループに分類しています。
# 最初に、すべての要素を unclassified にグループ化します。
# 白いポインターが青いポインターより小さい限り、最初から繰り返します。

# 白いポインターが赤の場合 (nums[white] == 0)、赤いポインターと交換し、白と赤のポインターの両方を前方に移動します。
# ポインターが白 (nums[white] == 1) の場合、要素は既に正しい場所にあるため、スワップする必要はなく、白いポインターを前方に移動するだけです。
# 白いポインターが青の場合、最新の未分類の要素と交換します。
# 他者の解答
class Solution:
    def sortColors(self, nums):
        red, white, blue = 0, 0, len(nums)-1
        
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
                