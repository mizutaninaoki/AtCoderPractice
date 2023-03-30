from collections import deque


class Solution:
    def romanToInt(self, s: str) -> int:
        que = deque()
        que.append(-1)
        ans = 0
        for i in s:
            if i == "M":
                ans += 800 if que[-1] == "C" else 1000
            elif i == "D":
                ans += 300 if que[-1] == "C" else 500
            elif i == "C":
                ans += 80 if que[-1] == "X" else 100
            elif i == "L":
                ans += 30 if que[-1] == "X" else 50
            elif i == "X":
                ans += 8 if que[-1] == "I" else 10
            elif i == "V":
                ans += 3 if que[-1] == "I" else 5
            elif i == "I":
                ans += 1

            que.append(i)
        return ans


# -------------------------
# 他者のコード
# -------------------------
class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number
