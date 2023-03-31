
class Solution:
    def isPalindrome(self, s: str) -> bool:
        normal_s = ""
        reversed_s = ""
        for i, j in zip(list(s.lower()), list(reversed(s.lower()))):
            if i.isalnum():
                normal_s += i
            if j.isalnum():
                reversed_s += j

        return normal_s.replace(' ', '') == reversed_s.replace(' ', '')


# 他者の解答
class Solution:
    def isPalindrome(self, s: str) -> bool:
    	s = [i for i in s.lower() if i.isalnum()]
        # 文字列を逆にする場合はs[::-1]を使う！！！
    	return s == s[::-1]
