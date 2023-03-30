class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tmp1 = []
        for i in range(m):
            tmp1.append(nums1[i])

        tmp2 = []
        for j in range(n):
            tmp2.append(nums2[j])

        nums1[:] = sorted(tmp1 + tmp2)




# その２
def merge_two_sorted_arrays(A: List[int], m: int, B: List[int], n: int) -> None:
    a, b, write_index = m-1, n-1, m + n - 1

    while b >= 0:
        if a >= 0 and A[a] > B[b]:
            A[write_index] = A[a]
            a -= 1
        else:
            A[write_index] = B[b]
            b -= 1

        write_index -= 1