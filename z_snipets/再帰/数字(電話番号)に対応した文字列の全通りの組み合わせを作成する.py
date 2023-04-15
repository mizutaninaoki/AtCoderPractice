# see: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
# 再帰+辞書
class Solution:
    def letterCombinations(self, digits):
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        # １文字の場合は、指定されたmappingのvalueの中のそれぞれの要素を返す
        if len(digits) == 1:
            return list(mapping[digits[0]])
        # 最後の文字以外で再帰して、最後から１文字ずつ削って再帰を進めていく
        prev = self.letterCombinations(digits[:-1])
        # 最後のdigitsの番号に対応する文字列だけ取得
        additional = mapping[digits[-1]]
        # 最後のdigitsの番号に対応する文字列(additional)と前までに作成した文字列のリスト(prev)の要素毎にそれぞれくっつけていく。
        return [s + c for s in prev for c in additional]

# DFS+再帰+辞書


class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        m = {"2": "abc", '3': "def", '4': "ghi", '5': "jkl",
             '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        ret = []
        self.dfs(m, digits, "", ret)
        return ret

    def dfs(self, m, digits, path, ret):
        # digitsが空の文字列であれば、その時点で各番号に対応した文字列の組み合わせが
        if not digits:
            ret.append(path)
            return
        # mの辞書のvalueでループを回し、その中でdigitsを１文字ずつ進めて、全部のパターンをpathにいれていく。
        for c in m[digits[0]]:
            self.dfs(m, digits[1:], path+c, ret)
