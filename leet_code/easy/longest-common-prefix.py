class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""

        l = list(zip(*strs))
        for idx, i in enumerate(l):
            if len(set(i)) == 1:
                ans += strs[0][idx]
            else:
                break
        return ans


# ---------------
# 他者の解答
# ---------------
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        pre = strs[0]

        for i in strs:
            # 文字列が同じかどうか後ろの文字を１文字づつ削りながら検証している
            while not i.startswith(pre):
                pre = pre[:-1]

        return pre
