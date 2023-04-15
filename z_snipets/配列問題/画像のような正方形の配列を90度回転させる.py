# see: https://leetcode.com/problems/rotate-image/description/
# 他者の解答(各行を逆順にしてから転置して、そのままmatrixに代入する
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[:] = map(list, zip(*matrix[::-1]))

# 自分の解答(zip(*matrix)を使って転置する)


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ans = []
        # 転置してから、各行を逆順にすると、90度回転した形になる
        for i in zip(*matrix):
            ans.append(list(reversed(i)))
        matrix[:] = ans
