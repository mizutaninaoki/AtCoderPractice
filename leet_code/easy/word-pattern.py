# 自分の解答
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        d = {}

        # パターンの長さとsの中の単語数が違う場合はFalse
        if len(pattern) != len(s):
            return False

        # まだ辞書に登録していない単語の場合、辞書に登録する。すでに登録済みのパターンの場合、
        # 辞書に登録されている単語と同じかどうかテェックする。
        for pa, st in zip(pattern, s):
            if not pa in d:
                d[pa] = st
            else:
                if d[pa] != st:
                    return False

        # パターンは違うけど、登録している単語の値が同じなものがないかチェック。
        if len(set(d.values())) != len(d.values()):
            return False
        return True


# itertools.zip_longestを使うパターン
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        from itertools import zip_longest

        s = s.split()

        # パターンの数とsの単語数は一緒でないといけない。
        # また、set(zip_longest(pattern,s))で(キー, 値)のペアで、キー(pattern)だけ重複しているもの、値(単語)だけ重複しているものがないか調べる。(len()の数が違っていたらどこかに重複がある)
        return (len(set(pattern)) ==
                len(set(s)) ==
                len(set(zip_longest(pattern,s))))