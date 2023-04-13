# see: https://leetcode.com/problems/pascals-triangle-ii/description/
# 自分の解答(与えられたrowIndexまでの段のパスカルの三角形を作成して、最後の段(rowIndexの段)のリストを返す方法)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # まずはrowIndexまでの段の三角形の作る
        pascal = [[1]*(i+1) for i in range(rowIndex+1)]
        for i in range(rowIndex+1):
            # 各段の両端は「１」で固定なので1からループさせる。
            # iが１以下(0と1の時)、つまり一段目と二段目は、iが1以下なので、range(1, 0)、もしくはrange(1, 1)となって、下のループは回らずスキップされる。
            for j in range(1, i):
                # 三角形の各段の要素に対して、上の段の２つの要素を足し合わせた値を入れていく(各段の両端は「１」で固定)
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        # numRowsまでの段のパスカルの三角形を上記で作成済みのため、最後の段、つまりrowIndexの段の数字のリストを返す
        return pascal[-1]

# 他者の回答


class Solution(object):
    def getRow(self, r):
        ans = [1]*(r+1)
        up = r
        down = 1
        for i in range(1, r):
            ans[i] = ans[i-1]*up/down
            up = up - 1
            down = down + 1
        return ans
