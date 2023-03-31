# integerを逆順にして、そのintを32桁のビット表現に変換(与えられたintegerに相当する32桁のビット表現を逆順にした際の、それに相当するintegerを返す問題)
# see: https://leetcode.com/problems/reverse-bits/
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n: int) -> int:
        # Pythonでintegerを32桁のビット表現に変換するには、'{0:032b}'.format(n)と表記します。
        # 変数nを32桁のビット表現に変換　→　逆順にソート　→　32桁のビット表現(２進数)をintに戻す という処理を行えばOKです。
        return int('{0:032b}'.format(n)[::-1], 2)