# see: https://leetcode.com/problems/set-matrix-zeroes/description/
# 自分の解答(zipで転置して解く解法)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        from itertools import zip_longest
        tmp = []
        matx = matrix
        for i in range(len(matx)):
            for j in range(len(matx[0])):
                # 値が0のマスの位置をtmpへ入れておく
                if matrix[i][j] == 0:
                    tmp.append([i, j])

            # 値が0のマスの行を全て0にする
            for i2, j2 in tmp:
                matx[i2] = [0] * len(matx[0])
            # 転置してから、値が0のマスの行を全て0にする
            matx = list(zip(*matx))
            for i2, j2 in tmp:
                matx[j2] = [0] * len(matx[0])
            # 転置を戻しておく
            matx = list(zip(*matx))

        # 最後に参照渡しのmatrix[:]に代入
        matrix[:] = matx
