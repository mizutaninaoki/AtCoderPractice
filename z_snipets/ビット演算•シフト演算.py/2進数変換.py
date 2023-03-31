# see: https://leetcode.com/problems/number-of-1-bits/description/
# bin(n)[2:]で２進数変換のみ行う場合
class Solution:
    def hammingWeight(self, n: int) -> int:
        from collections import Counter
        return Counter(bin(n)[2:])["1"]
