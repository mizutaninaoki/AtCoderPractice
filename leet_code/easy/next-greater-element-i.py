# 自分の解答(全探索)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in nums1:
            num_idx = -1
            # nums2の中でiと同じ値のインデックスを保管しておく
            for idx, j in enumerate(nums2):
                if i == j:
                    num_idx = idx

            # 保管しておいたインデックスより右側に、iより大きい値があればansへ追加。
            # なければ-1をansへ追加
            flag = True
            if num_idx != -1:
                for k in nums2[num_idx+1:]:
                    if k > i:
                        ans.append(k)
                        flag = False
                        break
            if flag:
                ans.append(-1)
        return ans


# 他者の解答(stackを使う)
# 基本的に問題は、nums1 で 4 に取り組んでいる場合、nums2 で最初に 4 を見つけ、そのインデックスから nums2 で 4 より大きい次の数を見つけることです。
# 解は常にリスト nums2 の反対側から来ていることがわかります。これにより、スタックを使用するように指示されます。
# 手順:
# nums2 をトラバースし、スタックの一番上に要素を格納し始めます。
# 現在の数がスタックの一番上よりも大きい場合、ペアが見つかりました。スタックのトップが現在の数値よりも小さくなるまで、スタックからポップし続けます。
# 一致するペアが見つかったら、現在の番号をスタックの一番上にプッシュします。
# 最終的に、nums2 にトラバースする要素がなくなったが、stack に要素がある場合、次に大きな要素が見つからなかったことを正当化できます。したがって、スタック内の残りの要素に -1 を設定します。
def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
	if not nums2:
		return None

	mapping = {}
	result = []
	stack = []
	stack.append(nums2[0])

	for i in range(1, len(nums2)):
		# if stack is not empty, then compare it's last element with nums2[i]
		while stack and nums2[i] > stack[-1]:
			# if the new element is greater than stack's top element, then add this to dictionary
			mapping[stack[-1]] = nums2[i]
			# since we found a pair for the top element, remove it.
			stack.pop()
		# add the element nums2[i] to the stack because we need to find a number greater than this
		stack.append(nums2[i])

	# if there are elements in the stack for which we didn't find a greater number, map them to -1
	for element in stack:
		mapping[element] = -1

	for i in range(len(nums1)):
		result.append(mapping[nums1[i]])
	return result
