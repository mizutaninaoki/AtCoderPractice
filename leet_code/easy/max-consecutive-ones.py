# 自分の解答
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        tmp = 0
        ans = 0
        for i in nums:
            if i == 1:
                # 配列の中の値が1だったら、tmpに1追加
                tmp += 1
                ans = max(ans, tmp)
            else:
                tmp = 0

        return ans
