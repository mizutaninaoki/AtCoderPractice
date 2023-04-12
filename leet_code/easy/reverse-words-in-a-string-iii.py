class Solution:
    def reverseWords(self, s: str) -> str:
        tmp = ""
        ans = ""
        for i in s:
            # 空白であれば、tmpに保持しておいた文字を逆順にしてansに追加する
            if i == " ":
                ans += "".join(tmp[::-1]) + i
                tmp = ""
            else:
                tmp += i

        # 最後tmpに残っていたら、逆順にしてansにくっつける
        ans += "".join(tmp[::-1])
        return ans
