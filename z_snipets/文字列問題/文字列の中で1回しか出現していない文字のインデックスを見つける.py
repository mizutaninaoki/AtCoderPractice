# see: https://leetcode.com/problems/first-unique-character-in-a-string/
# dictを使った方法
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
