# 自分の解答(転置)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        while matrix:
            ans += matrix[0] # 一番最初(上)の行をansに追加
            matrix.pop(0)
            # matrixを転置してから列の並びを逆順にしておき、次のループでスパイラルのように配列の値がansに格納されるようにする。
            matrix = list(zip(*matrix))[::-1]
        return ans