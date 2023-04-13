# see: https://leetcode.com/problems/valid-anagram/description/
# ２つの文字列がお互いアナグラムかどうかチェック
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        return Counter(s) == Counter(t)


# sortedを使う方法
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
