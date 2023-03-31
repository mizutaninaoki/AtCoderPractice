# "{0:032b}".format(n)で２進数変換 & 32ビット変換を使う場合
class Solution:
    def hammingWeight(self, n: int) -> int:
        from collections import Counter
        return Counter("{0:032b}".format(n))["1"]

# bin(n)[2:]で２進数変換のみ行う場合


class Solution:
    def hammingWeight(self, n: int) -> int:
        from collections import Counter
        return Counter(bin(n)[2:])["1"]
