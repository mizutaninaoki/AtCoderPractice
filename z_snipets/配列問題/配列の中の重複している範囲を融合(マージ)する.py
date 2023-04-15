# see: https://leetcode.com/problems/merge-intervals/description/
# 自分の解答
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        # ソートして、intervalsの各配列の中の0番目の要素は必ず昇順にならんでいるようにする
        intervals.sort()
        prev = intervals[0]
        # 最初のリストの範囲以外をループ
        for i in intervals[1:]:
            # 前の範囲の最大値が、今回の範囲の最小値より小さい場合、被っている範囲はないので、そのままansに追加する
            if prev[1] < i[0]:
                ans.append(prev)
                prev = i
            else:
                # 0番目の要素はソートしているため必ずprev[0]が一番小さい値になっているが、
                # 1番目の要素はprev[1]とi[1]、どちらが大きい値になるかわからないので、max()で大きい値をprev[1]の値にする。
                prev[1] = max(prev[1], i[1])

        # 最後の要素がまだ残っているため、ansに追加しておく
        ans.append(prev)
        return ans


# 他者の解答
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for i in intervals:
            if not merged or merged[-1][-1] < i[0]:
                merged.append(i)
            else:
                merged[-1][-1] = max(merged[-1][-1], i[-1])
        return merged
