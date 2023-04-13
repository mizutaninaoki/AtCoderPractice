# sの文字列を先頭から辞書のキーに保存していって、valueにはその文字が出現したインデックスを入れる。
# valueのインデックスを更新しながら、一番長いnon-repeated substringを探していく方法。
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic, res, start, = {}, 0, 0
        for i, ch in enumerate(s):
            # ループで回ってきたsの中の文字がdicのキーに存在する場合
            if ch in dic:
                # 文字列の先頭からインデックスまでの長さをチェックする
                # (iもstartもともにインデックスを表しているため、両方0から始まる数字。だからi-startで正しくnon-repeated substringの長さの計算できる。)
                res = max(res, i-start)  # update the res
                # 文字列の先頭のインデックスを次のインデックスに更新する(次のインデックスに更新するから「dic[ch]+1」で+1している)
                # here should be careful, like "abba"
                start = max(start, dic[ch]+1)
            # 文字列を辞書に追加・更新する。
            dic[ch] = i
        # 答えは、文字列の先頭/中間、または中間から末尾のいずれかにある
        # return should consider the last non-repeated substring
        return max(res, len(s)-start)
