# see: https://leetcode.com/problems/number-of-1-bits/description/
# "{0:032b}".format(n)で２進数変換 & 32ビット変換を使う場合
class Solution:
    def hammingWeight(self, n: int) -> int:
        from collections import Counter
        return Counter("{0:032b}".format(n))["1"]
