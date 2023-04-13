# see: https://leetcode.com/problems/longest-palindrome/description/
# 自分の解答
class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        counter = Counter(s)

        flag = False
        ans = 0
        for k, v in counter.items():
            # 出現回数が偶数の文字の場合、出現回数をそのままansへ足し合わせる
            if v % 2 == 0:
                ans += v
            # 出現回数が奇数の文字の場合、flagをTrueにして、偶数回分だけansへ足し合わせる
            else:
                flag = True
                ans += v - 1

        # 奇数の出現回数の文字が１つでもある場合、回文の真ん中の文字に使えるため、ansにプラス1する
        if flag:
            ans += 1
        return ans
