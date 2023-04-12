class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans = []
        for c in s:
            # ansの最後の文字がループしてきた文字と同じであれば、ans最後の文字を削除して、同じ文字が２回並ぶことがないようにする。
            if ans and ans[-1] == c:
                ans.pop()
            else:
                ans.append(c)
        return ''.join(ans)