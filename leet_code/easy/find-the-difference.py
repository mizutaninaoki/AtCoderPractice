# 自分の解答
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter
        cs = Counter(s)
        ct = Counter(t)
        for i in ct:
            # countの数が違う(Counterは存在しないキーの場合、0を返す)キーの文字を返す
            if ct[i] != cs[i]:
                return i
