# see: https://leetcode.com/problems/backspace-string-compare/description/
# 自分の解答
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s2 = []
        t2 = []

        for i in s:
            if i == "#":
                if len(s2):
                    s2.pop()
            else:
                s2.append(i)

        for j in t:
            if j == "#":
                if len(t2):
                    t2.pop()
            else:
                t2.append(j)
            print(t2)

        return "".join(s2) == "".join(t2)
