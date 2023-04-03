# 自分の解答(dictを使う方法)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import defaultdict
        d = defaultdict(int)
        # 辞書に出現した文字をきーにして、その文字のインデックスと出現回数を記録
        for idx, i in enumerate(s):
            if not d[i]:
                d[i] = [idx, 1]
            else:
                d[i][1] += 1

        l = []
        # 出現回数が１回であれば。lの配列にあれておいて、その中で一番インデックス番号が小さい値を返す
        for idx, j in d.items():
            if j[1] == 1:
                l.append(j[0])

        return min(l) if l else -1

# dictを使ったもう少しスマートな方法


class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for l in s:
            if l not in d:
                d[l] = 1
            else:
                d[l] += 1

        index = -1
        # 文字列を頭から回していき、最初に出現回数が1だった文字のインデックスを返す
        for i in range(len(s)):
            if d[s[i]] == 1:
                index = i
                break

        return index

# Counterを使う方法


class Solution(object):
    def firstUniqChar(self, s):
        import collections
        hset = collections.Counter(s)
        # Traverse the string from the beginning...
        for idx in range(len(s)):
            # If the count is equal to 1, it is the first distinct character in the list.
            if hset[s[idx]] == 1:
                return idx
        return -1       # If no character appeared exactly once...
