# パスカルの三角形
# https://ja.wikipedia.org/wiki/%E3%83%91%E3%82%B9%E3%82%AB%E3%83%AB%E3%81%AE%E4%B8%89%E8%A7%92%E5%BD%A2
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # まずはnumRowsで指定された段の三角形の作る
        pascal = [[1]*(i+1) for i in range(numRows)]
        for i in range(numRows):
            # 各段の両端は「１」で固定なので1からループさせる。
            # iが１以下(0と1の時)、つまり一段目と二段目は、iが1以下なので、range(1, 0)、もしくはrange(1, 1)となって、下のループは回らずスキップされる。
            for j in range(1, i):
                # 三角形の各段の要素に対して、上の段の２つの要素を足し合わせた値を入れていく(各段の両端は「１」で固定)
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        return pascal


class Solution:
    def generate(self, n: int) -> List[List[int]]:
        ans = [[1]*i for i in range(1, n+1)]   # initialize triangle with all 1
        for i in range(1, n):
            for j in range(1, i):
                # update each as sum of two elements from above row
                ans[i][j] = ans[i-1][j] + ans[i-1][j-1]
        return ans
