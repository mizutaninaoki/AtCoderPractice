class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        first = 0
        last = len(s) - 1
        while last > first:
            # インデックスを指定してsを更新していく場合は、引数のsで山椒私で渡ってきたやつでも変更される。
            s[first], s[last] = s[last], s[first]
            first += 1
            last -= 1

# [::-1]を使うパターン


class Solution:
    def reverseString(self, s: List[str]) -> None:
        # 引数のs全体を丸ごと書き換える場合は、s[:]にしないと書きかわらない
        s[:] = s[::-1]
