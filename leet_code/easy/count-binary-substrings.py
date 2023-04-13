class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans, prev, cur = 0, 0, 1
        for i in range(1, len(s)):
            # 前の連続する値の長さと今回の連続する値の長さの小さい方をansに足し合わせていく(なぜこのようなことをするかは一番下の「自分の解釈」を参考)
            if s[i] != s[i - 1]:
                ans += min(prev, cur)
                prev = cur
                cur = 1
            # 現在の文字が前の文字と等しい場合 - 現在の連続カウントをインクリメントするだけです
            else:
                cur += 1
        ans += min(prev, cur)
        return ans

# 以下は解説に載っていた例
# see: https://leetcode.com/problems/count-binary-substrings/solutions/1172569/short-easy-w-explanation-comments-keeping-consecutive-0s-and-1s-count-beats-100/
# 1. 0011
# In this string, consecutive count of binary characters are [2, 2]. We can form a total of 2 substrings.

# 2. 00011
# In this string, consecutive count of binary characters are [3, 2]. Still, we can only form 2 substrings.

# 3. 000111
# Here, consecutive count of binary characters are as - [3,3]. Now, we can form 3 substrings.

# 4. 00011100
# Consecutive count of binary characters are - [3,3,2]. We can form 3 substrings with the first 2 groups of zeros and ones.
# Then we can form 2 substrings with the latter 2 groups. So, a total of 5 substrings.

# 5. 00011100111
# Consecutive count - [3,3,2,3]. Substrings formed - 3 + 2 + 2 = 7
# 上記の例から、最終的なカウントはバイナリ文字の連続カウントのみに依存することがわかります。連続する文字の 2 つのグループごとに、形成できる部分文字列の数は、2 つのグループ間で count の最小値になります。

# ここで、すべてのグループ化とそのカウントを維持してから、部分文字列の数をカウントできますが、実際にはすべての文字列で連続したカウントを維持する必要さえありません。現在の連続カウントと以前の連続カウントを保存し、その場で部分文字列をカウントできます。


# -------------------
# 自分の解釈
# -------------------
# つまり、最後の5の例で言えば、00011100111の場合、連続する数字の出現回数をリストにまとめると、[3,3,2,3]。
# これをリスト内の前から２つの数字ずつを比較していって、小さい方の数字を足していけば、連続する0と1の数が等しい部分文字列の数を算出することができる。
# [3,3,2,3]
# ↓
# 「3と3」、「3と2」、「2と3」をそれぞれ比較して、それぞれの小さい方を全て足す、つまり「3+2+2」となり、答えは7となる。
