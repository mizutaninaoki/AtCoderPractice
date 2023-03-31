# 符号なし整数型 【uint型】 unsigned integer type
# 符号なし整数型とは、整数を格納するデータ型の一種で、0と正の数のみを表現できる整数型。単純に全ビットを2進数の各桁に対応付けて数を表す。

# integerを逆順にして、そのintを32桁のビット表現に変換(与えられたintegerに相当する32桁のビット表現を逆順にした際の、それに相当するintegerを返す問題)
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n: int) -> int:
        # Pythonでintegerを32桁のビット表現に変換するには、'{0:032b}'.format(n)と表記します。
        # 変数nを32桁のビット表現に変換　→　逆順にソート　→　32桁のビット表現(２進数)をintに戻す という処理を行えばOKです。
        return int('{0:032b}'.format(n)[::-1], 2)

# ビット演算・シフト演算だけで行う方法


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        # resの変数にnの下一桁の値に対して、AND演算(1と1のときのみ1を返す。それ以外は0を返す)を行い、行った後はnを右に１桁ずらす。これを32回行って、nを32ビットに変換する。
        for _ in range(32):
            # res<<1:1桁だけ左にずらし、空いたビットに0が入る, n&1:下1桁の値だけ取り出す
            res = (res << 1) + (n & 1)
            n >>= 1  # n>>1: 1桁だけ右にずらし、押し出された下1桁のビットは消える
        return res
