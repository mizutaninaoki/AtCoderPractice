# bisect(二分探索no
# ライブラリを使う方法
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        from bisect import bisect_left
        # listをsetに変換して、次のin演算を高速にしている（in演算が５回未満の場合、set型に変換するコストの方が大きく、低速になるらしいが。。。）
        s = set(nums)
        return bisect_left(nums, target) if target in s else -1

# 二分探索を描く方法


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left+right)//2  # インデックスの真ん中
            # targetがリストの真ん中の値(nums[mid])と同じであれば、その値のインデックスを返す
            if nums[mid] == target:
                return mid
            # targetが真ん中の値よりも大きい場合、配列の左側のどこかにtargetがある可能性があるため、
            # 左側の配列最大のインデックスを今の真ん中のインデックス(mid)を除いた(１つ左にずらす)インデックスにして再度二分探索を行う
            elif nums[mid] > target:
                right = mid-1
            # targetが真ん中の値よりも小さい場合、配列の右側のどこかにtargetがある可能性があるため、
            # 右側の配列最小のインデックスを今の真ん中のインデックス(mid)を除いた(１つ右にずらす)インデックスにして再度二分探索を行う
            else:
                left = mid+1

        return -1
