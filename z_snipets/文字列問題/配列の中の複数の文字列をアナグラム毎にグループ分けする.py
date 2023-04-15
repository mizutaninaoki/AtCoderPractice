# see: https://leetcode.com/problems/group-anagrams/description/
# 他者の解答(ソートしてから辞書に記憶する)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for word in strs:
            # アナグラムをソートして、同じ文字に変換する
            sortedWord = ''.join(sorted(word))
            # 辞書に登録していない文字列であれば登録して、すでに登録済みであればそのキーに追加する。
            if sortedWord not in h:
                h[sortedWord] = [word]
            else:
                h[sortedWord].append(word)

        # 辞書にキー毎にまとめたvaluesを提出用にfinalの配列にまとめる
        final = []
        for value in h.values():
            final.append(value)
        return final
