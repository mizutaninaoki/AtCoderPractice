# see: https://leetcode.com/problems/valid-sudoku/description/
# それぞれのメソッドに切り分けた解き方
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (self.is_row_valid(board) and
                self.is_col_valid(board) and
                self.is_square_valid(board))

    # 盤全体の行が有効かどうか
    def is_row_valid(self, board):
        for row in board:
            if not self.is_unit_valid(row):
                return False
        return True

    # 盤全体の列が有効かどうか
    def is_col_valid(self, board):
        # zip(*board)で転置している
        for col in zip(*board):
            if not self.is_unit_valid(col):
                return False
        return True

    # 3×3の盤面の中が有効かどうか
    def is_square_valid(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                # 3×3だけ順番に抽出してsquareの中に入れている
                square = [board[x][y]
                          for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.is_unit_valid(square):
                    return False
        return True

    # 1行、もしくは1列の中で「.」以外で同じ数字が出現していないかチェックするメソッド
    def is_unit_valid(self, unit):
        unit = [i for i in unit if i != '.']
        return len(set(unit)) == len(unit)


# Counterを使った解法(短いけどよくわからん)
class Solution:
    def isValidSudoku(self, board):
        import collections
        return 1 == max(collections.Counter(
            x
            for i, row in enumerate(board)
            for j, c in enumerate(row)
            if c != '.'
            for x in ((c, i), (j, c), (i/3, j/3, c))
        ).values() + [1])
