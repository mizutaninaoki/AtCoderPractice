# see: https://leetcode.com/problems/move-zeroes/description/
# in-place
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero = 0  # 最初の0のポジションは0に設定
        for i in range(len(nums)):
            # 0でない場合はzeroのポジションを１進める。
            # 0の時はzeroのポジションは進まず、iのポジション(インデックス)だけ進んでいく。
            # 感覚としては0を一つ右にスラしながら、zeroのポジションも１つずつ進めていくイメージ(以下遷移図参考)
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1

# moveZeroesの遷移は以下のようにされる
# [0, 1, 0, 3, 12]
# --------------
# [1, 0, 0, 3, 12]
# --------------
# [1, 0, 0, 3, 12]
# --------------
# [1, 3, 0, 0, 12]
# --------------
# [1, 3, 12, 0, 0]
# --------------
