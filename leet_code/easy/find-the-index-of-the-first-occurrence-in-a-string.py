class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle in haystack:
            return -1

        ans = 0
        for i in range(len(haystack)):
            if haystack[i:len(needle)+i] == needle:
                ans = i
                break
        return ans