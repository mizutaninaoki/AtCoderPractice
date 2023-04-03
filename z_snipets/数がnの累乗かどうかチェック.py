# see: https://leetcode.com/problems/power-of-three/description/
# 3でひたすら割り算するやり方
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            # 3の0乗は1なのでTrue
            return True

        while n % 3 == 0:
            n //= 3

        # 最後nが3の累乗の数であれば、3//3=1になっているはず
        return n == 1


# n = 3 ^ i
# i = log3(n)
# i = log(n) / log(3) logの変換公式
# see: https://leetcode.com/problems/power-of-three/solutions/2471488/quick-math/
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        import math
        return n > 0 and (math.log10(n) / math.log10(3)) % 1 == 0
