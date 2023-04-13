# 他者の解答(unicodeを使った解答)


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def str2int(num):
            result = 0
            # numをループで回すと、くらいの大きい数を先頭にループが回る
            # そのため、result * 10で都度、位を１つ上に上げて、ord(n) - ord("0")の差、つまりはその桁の数の数字を出す。
            # ここではループで回してややこしくなっているが、結局このループでint()を使わず、文字列を整数に変換している。
            for n in num:
                # 以下はord()の例
                # ord("0")
                # 48
                # ord("1")
                # 49
                # ord("2")
                # 50
                result = result * 10 + ord(n) - ord("0")
            return result

        return str(str2int(num1) + str2int(num2))

# 他者の解答(辞書を使った解答)


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        def str2int(num):
            numDict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                       '6': 6, '7': 7, '8': 8, '9': 9}
            output = 0
            for d in num:
                output = output * 10 + numDict[d]
            return output

        return str(str2int(num1) + str2int(num2))
