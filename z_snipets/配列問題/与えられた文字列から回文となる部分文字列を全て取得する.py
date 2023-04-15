# see: https://leetcode.com/problems/palindrome-partitioning/description/
# 他者の解答(再帰)
class Solution:
    @cache  # the memory trick can save some time
    def partition(self, s: str) -> List[List[str]]:
        # 再帰してきて、sが空文字であれば、二重のからのリストを返す
        if not s:
            return [[]]
        ans = []
        # ループを回して、先頭の文字から１文字ずつ範囲を広めて、その中に回文の文字列がないかチェックしていく
        for i in range(1, len(s) + 1):
            # 現在の部分文字列が回文かどうかチェック
            if s[:i] == s[:i][::-1]:
                # 左側s[:i]が回文だったら、右側の文字列で再帰させて、そちらにも回文がないかチェックする。
                # 右側の文字列で回文の部分があったら、その部分を全てリストで返ってくるため、forループの中で現在の左側の回文(s[:i])と右側の回文(suf)をくっつける。(回文と回文をくっつけても、１つの回文になるため。)
                # 右側の文字列に回文部分がなければ、空の二重配列([[]])が再帰で返ってくるため、forループの中でapppendされるのは左側の回文文字列(s[:i]])のみとなる。
                for suf in self.partition(s[i:]):
                    ans.append([s[:i]] + suf)
        return ans
