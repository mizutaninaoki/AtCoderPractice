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

# 自分の解答(TLE)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter

        ans = []
        idx = 0
        while len(strs) != 0:
            ci = Counter(strs[idx])
            tmp = [strs[idx]]

            for j in range(idx+1, len(strs)):
                cj = Counter(strs[j])
                # ciとcjの構成要素をカウントして、その結果が全く同じであれば(アナグラムであれば)、tmpに追加
                if ci == cj:
                    tmp.append(strs[j])

            # ansにtmpの結果を追加して、すでに検証したアナグラムの文字列はstrs.remove(k)で削除する
            ans.append(tmp)
            for k in tmp:
                strs.remove(k)      

        return ans
