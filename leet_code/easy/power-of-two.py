# 自分の解法(math.log2(n)を使う方法)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        import math
        if n == 1:
            return 1
        # nがマイナスの時、もしくはnが奇数のときは、必ず2の累乗にはならない。
        if n % 2 != 0 or n <= 0:
            return False

        log2_num = math.log2(n)
        # log2_numがfloatになれば、2の累乗の値でないことがわかる。
        if int(log2_num) == log2_num:
            return int(log2_num)
        else:
            return False


# 2の累乗を２進数に直すと、必ず先頭が1、他の数字は0になるのを利用する方法
# 解説：https://leetcode.com/problems/power-of-two/solutions/948641/python-o-1-solution/
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and sum(list(map(int, bin(n)[2:]))) == 1


# ビット演算を使う方法
# 解説: https://leetcode.com/problems/power-of-two/solutions/948641/python-o-1-solution/
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n-1) == 0

#      <----- binary ---->
#  n      n    n-1   n&(n-1)
# --   ----   ----   -------
#  0   0000   0111    0000 *
#  1   0001   0000    0000 *
#  2   0010   0001    0000 *
#  3   0011   0010    0010
#  4   0100   0011    0000 *
#  5   0101   0100    0100
#  6   0110   0101    0100
#  7   0111   0110    0110
#  8   1000   0111    0000 *
#  9   1001   1000    1000
# 10   1010   1001    1000
# 11   1011   1010    1010
# 12   1100   1011    1000
# 13   1101   1100    1100
# 14   1110   1101    1100
# 15   1111   1110    1110
# 0および 2 のべき乗 ( 1、2、4および8) のみがビット パターンになり0000/false、その他はすべて非ゼロまたは であることがわかりますtrue。
