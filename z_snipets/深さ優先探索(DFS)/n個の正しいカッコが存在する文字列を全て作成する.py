# see: https://leetcode.com/problems/generate-parentheses/description/
# 1.有効な'('の後にのみ')'を追加することです。
# 2.2つの整数変数leftとrightを使って、現在の文字列の中に'('と')'がいくつあるか確認します。
# 3.left < nの場合、現在の文字列に'('を追加することができます。
# 4.右＜左の場合、現在の文字列に')'を追加することができます。
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # left = 開く側のカッコの文字数
        # right = 閉じる側のカッコの文字数
        # s = 現在再帰で回ってきている時のleftとrightを合計した文字数
        def dfs(left, right, s):
            # 「n * 2」でカッコの全ての文字列の文字数になる。(n = 2なら、"(())"みたいなカッコがOKで、文字数は4文字になる)
            # len(s) == n * 2が成立する時、指定されたカッコの形をした文字列になっている。
            if len(s) == n * 2:
                res.append(s)
                return

            # nの数よりもleftが小さければ条件には合わないので、まずはleftをn以上の数追加していく。
            if left < n:
                dfs(left + 1, right, s + '(')

            # rightがleft未満であれば、正しいカッコの形にならないため、rightのカッコを追加する。
            if right < left:
                dfs(left, right + 1, s + ')')

        res = []
        dfs(0, 0, '')
        return res

# dfs()には引数のsが以下のような形で再帰されていく
# (
# ((
# (((
# ((()
# ((())
# ((()))
# (()
# (()(
# (()()
# (()())
# (())
# (())(
# (())()
# ()
# ()(
# ()((
# ()(()
# ()(())
# ()()
# ()()(
# ()()()
