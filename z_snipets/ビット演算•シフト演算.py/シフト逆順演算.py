# integerを逆順にして、そのintを32桁のビット表現に変換(与えられたintegerに相当する32桁のビット表現を逆順にした際の、それに相当するintegerを返す問題)
# see: https://leetcode.com/problems/reverse-bits/
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        # resの変数にnの下一桁の値に対して、AND演算(1と1のときのみ1を返す。それ以外は0を返す)を行い、行った後はnを右に１桁ずらす。これを32回行って、nを32ビットに変換する。
        for _ in range(32):
            # res<<1:1桁だけ左にずらし(逆順にするため)、空いたビットに0が入る, n&1:下1桁の値だけ取り出す
            res = (res << 1) + (n & 1)
            n >>= 1  # n>>1: 1桁だけ右にずらし、押し出された下1桁のビットは消える
        return res
