# see: https://leetcode.com/problems/longest-consecutive-sequence/description/
# 自分の解答'(sortとset使う)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 重複をなくす
        nums = sorted(list(set(nums)))
        if not nums:
            return 0

        ans = 0
        prev = nums[0]
        tmp_max = 1
        # 現在の値が「前の値+1」の値かどうかチェックして、プラス1ずつで連続する値の最大の長さを測る
        for i in range(1, len(nums)):
            if nums[i] == prev + 1:
                tmp_max += 1
            else:
                ans = max(ans, tmp_max)
                tmp_max = 1
            prev = nums[i]
        # 最後、tmp_maxにプラス1ずつで連続する値の最大の長さが入っているかもしれないため、max(ans, tmp_max)する
        ans = max(ans, tmp_max)
        return ans

# 他者の解答(ソートせずsetのみで解く方法)


class Solution:
    def longestConsecutive(self, nums):
        s, longest = set(nums), 0
        # リストの中の要素毎にループを回す
        for num in s:
            # 今の値より1小さい値が存在すればスキップする。
            # (つまり、連続する値たちの中の最小値以外の場合、そこから数えても意味がないため、スキップする)
            if num - 1 in s:
                continue

            # 連続する値が1つの場合でもjは1なので、j=1から始める(j=0ではない！)
            j = 1
            # ここのnumには必ず連続する値たち(1つしか値がない場合も含む)の最小値が入っている。
            # その最小値から1ずつ足していって、その値と同じ値があればjにプラス1して、なければ連続する値がないので、その時点での最大の長い方の長さをlongestに入れる
            while num + j in s:
                j += 1
            longest = max(longest, j)
        return longest
