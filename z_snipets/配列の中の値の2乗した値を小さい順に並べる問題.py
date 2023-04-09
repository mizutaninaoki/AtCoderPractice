# see: https://leetcode.com/problems/squares-of-a-sorted-array/description/
# O(n)なやり方。queを使って、両端の数字を大きい順に並べて、最後に逆順にするやり方
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        from collections import deque
        que = deque(nums)
        reverse_sorted_squares = []

        # キューの両端の数字を２乗して、大きい方をreverse_sorted_squaresに追加していく。
        # すると、２乗した数の大きい順に追加されていくので、最後に逆順にしてreturnする
        while que:
            left = que[0] ** 2
            right = que[-1] ** 2

            if left > right:
                reverse_sorted_squares.append(left)
                que.popleft()
            else:
                reverse_sorted_squares.append(right)
                que.pop()

        return reverse_sorted_squares[::-1]

# 一旦2乗にして、最後にソートする古典的なやり方(この方法で本番は解かないようにしたい)


def sortedSquares(self, A: List[int]) -> List[int]:
    return sorted([v**2 for v in A])
