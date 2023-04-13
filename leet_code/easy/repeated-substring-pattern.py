# 他者の回答
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # 与えられた文字列の最初以外の文字列と、最後以外の文字列をくっつけた文字列の中に、与えられたsも文字列が存在すれば、sの中の一部分の文字列が繰り返されていることがわかる。
        # (最初と最後の文字を削った文字列はそれぞれsの文字列の１文字かけた文字列。その２つの文字列を繋げると、sがrepeatedな文字列の場合、真ん中にsの文字列が含まれているはず)
        return s in s[1:] + s[:-1]

# s = "abcabcabcabc"
# s[1:]
# 'bcabcabcabc'
# s[:-1]
# 'abcabcabcab'
# s[1:] + s[:-1]
# 'bcabcabcabcabcabcabcab'
# s in s[1:] + s[:-1]
# True
