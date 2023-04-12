# see: https://leetcode.com/problems/find-the-town-judge/description/
# アルゴリズム：-
# 町の総人口を表すTrustedサイズの配列を作成し、それを 0 で初期化します。N+1
# 初期化後、人が自分以外の誰かを信頼するときはいつでも、trustedその人は質問で言及された 2 つの条件を満たさないため、その人の価値を下げる必要があります。
# また、あるx人が街の人から信頼されていれば、そのx人の価値は上がり、そのx人を信頼していた人の価値は下がるはずです。
# 最後に街中の人を縦横無尽に横断し、横断中に人が見つかれば、N-1 trustsその人が判断し、その人のインデックスを返します。
# see: https://leetcode.com/problems/find-the-town-judge/solutions/1663344/c-java-python3-javascript-everything-you-need-to-know-from-start-to-end/?orderBy=most_votes&languageTags=python3
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        Trusted = [0] * (N+1)
        # Trustedの最初の要素に、trustの要素分(信頼している人を表す配列分)マイナス1して、Trustedの最後の要素にはプラス1しておく
        for (a, b) in trust:
            Trusted[a] -= 1
            Trusted[b] += 1
        
        # 以下のコードのアルゴリズム、よく理解してない。。。
        for i in range(1, len(Trusted)):
            if Trusted[i] == N-1:
                return i
        return -1
    