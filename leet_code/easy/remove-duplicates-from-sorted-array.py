class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = []
        for i in sorted(nums):
            if len(l) == 0 or l[-1] != i:
                l.append(i)

        # 答え方として、与えられた引数の配列を変更する場合、[:]をつけて代入しなくてはいけない。
        nums[:] = l
        return len(nums)

# nums = 元リストの要素を置き換えない。
# nums[:] = 所定の位置にある要素を置き換える。
# 要するに、[:]がないと、新しいリストオブジェクトを作ることになり、この問題が求めていることに反しているのです：
# "別の配列のために余分な領域を確保しないでください。O(1)個の余分なメモリを使って、入力配列をインプレースで修正する必要があります。"

#------------
# 他者の解答
#------------
class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		nums[:] = sorted(set(nums))
		return len(nums)