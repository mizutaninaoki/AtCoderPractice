# 自分の解答。簡単なやり方
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # intの第二引数に、第一引数の進数を指定すると(デフォルトは10進数)、その進数の値を10進数に変換してくれる
        sum_num = int(a, 2) + int(b, 2)
        return bin(sum_num)[2:]


# ２進数同士の足し算を１からやる方法
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # ２進数の足し算において、1+1で溢れ出す場合(２進数において、数字は0と1しかないため、一つ上の桁の数にプラス１される)
        # 、溢れ出して一つ上の桁の数に1を足すこの「１」のことを「桁上りのビット=キャリービット」という。
        carry = 0
        result = ''

        a = list(a)
        b = list(b)

        # ２つの２進数の下一桁から順に足していく(２進数の足し算)
        while a or b or carry:
            # aの配列最後の数が「1」であれば変数carryにプラス１する
            if a:
                carry += int(a.pop())
            # bの配列最後の数が「1」であれば変数carryにプラス１する
            if b:
                carry += int(b.pop())

            # carry % 2で算出された数が、この桁の数となる。
            # 「carry % 2 == 0」 -> 0 (このとき、carryは0か2)
            # 「carry % 2 == 1」 -> 1 (このとき、carryは必ず1)
            result += str(carry % 2)
            # 桁上がりの場合(つまり、carryが2の場合)、次の上の桁にプラス1足して２進数の計算を行う必要があるため、「carry //= 2」を行う。
            # 「carry //= 2」 -> 0 (このとき、carryは0か1)
            # 「carry //= 2」 -> 1 (このとき、carryは必ず2。次の桁の計算のcarryのデフォルト値は1にする)
            carry //= 2

        # ２進数の足し算は、２で割った余りをつなげて、逆順に読む必要がある。（これ10進数を２進数に変換した時のやり方だけど、この場合も最後に逆から読み必要があるっぽい。よくわからない。。。）
        return result[::-1]
