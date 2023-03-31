class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # ord("A")
        # # 65
        # ord("Z")
        # # 90

        res = 0
        for c in columnTitle:
            # １桁大きくなるにつれてA~Zまで26文字あるから、26通り選択肢が増える。そのため、今までの文字の組み合わせと26を掛け合わせる必要がある。
            res = res * 26 + ord(c) - ord("A") + 1
        return res