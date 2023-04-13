# see: https://leetcode.com/problems/ransom-note/description/
# 他者の回答(共通部分で考える)
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        from collections import Counter
        st1, st2 = Counter(ransomNote), Counter(magazine)
        # ransomNoteとmagazineの共通要素が、まるまるransomNoteであればTrue
        if st1 & st2 == st1:
            return True
        return False


# 自分の解答
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        counter_r = Counter(ransomNote)
        counter_m = Counter(magazine)

        for i in counter_r:
            # ransomNoteに使われている文字が、magazineの中になければFalse
            if not i in counter_m:
                return False
            # ransomNoteに使われている文字の数に、magazineの中の特定の文字数が達していなければFalse
            if counter_m[i] < counter_r[i]:
                return False
        return True
