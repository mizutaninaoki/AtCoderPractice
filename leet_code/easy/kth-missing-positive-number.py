# 自分の方法(WA)
# class Solution:
#     def findKthPositive(self, arr: List[int], k: int) -> int:
#         cnt = 0
#         idx = 0
#         ans = 0
#         for i in range(1, 1001):
#             if idx < len(arr) and arr[idx] == i:
#                 idx += 1
#                 continue
#             else:
#                 cnt += 1
#                 if cnt == k:
#                     ans = i
#                     break
#         return ans

# 二分探索を使った方法
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = low + (high - low) // 2
            # 理想的には、arr[i]はi + 1の値を保持する必要があります。つまり、arr[0] = 1, arr[1] = 2.などです。
            # つまり、真ん中のインデックス(mid)までに抜けている数の個数をmissingに代入している。midのインデックスは0から始まるため、+1して調整している。
            missing = arr[mid] - (mid + 1)
            # 抜けている数字の数がkより大きければ、リストの左側に移動し、小さければ、右側に移動する。
            if missing >= k:
                high = mid - 1
            else:
                low = mid + 1
        # 「high+1」は抜けている数でk番目にくる値のインデックスとなる。そして、kには抜けている数の中で指定されたインデックスの数が指定されている。
        # つまり、本来arr[0] = 1, arr[1] = 2、みたいな形であれば、「high + 1 + k」番目の値が抜けている数の中でもk番目の値となる。
        return high + 1 + k


# 単純な方法
class Solution:
	def findKthPositive(self, arr: List[int], k: int) -> int:
		arr = set(arr)
		for i in range(1, len(arr)+k+1):  # O(n+k)
			if i not in arr:
				k -= 1
			if k == 0:
				return i

# bisect_rightを使った方法


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        from bisect import bisect_right
        return bisect_right(range(len(arr)), k, key=lambda x: arr[x] - x) + k
