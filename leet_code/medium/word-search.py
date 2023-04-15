# 他者の解答(DFS)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    # (i,j)の位置で開始し、単語が見つかるかどうかをチェックする。
    def dfs(self, board, i, j, word):
        if len(word) == 0:  # 全文字のチェックが完了したらTrue
            return True
        # 列と行がマス目からはみ出る、もしくは、現在引数に渡ってきているwordの文字(最初の文字)と違う文字であればFalse
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        # 今いる位置の文字をtmpに一時保管しておいて、board[i][j]には"#"を入れて、一度来たboardの位置には再度こないようにする。
        # (下の方のコードで上下左右のマス目に次のwordのアルファベットがないか探すようにしているため、"#"を入れておけば、word[0]!=board[i][j]でFalseが返される。
        # となりのマス目の探索が完了したら、board[i][j] = tmpで今のマス目のアルファベットを元に戻す)
        tmp = board[i][j]
        board[i][j] = "#"

        # 上下左右に次のwordのアルファベットがないか再帰で探索する
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) or self.dfs(
            board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        # となりのマス目の探索が完了したら、今のマス目のアルファベットを元に戻す。(もしかすると途中でルートが２つとかに分岐した時に、"#"から元の文字に戻しとかないと、おかしいことになるため)
        board[i][j] = tmp
        return res

# 自分の解答(WA)
# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         start = []
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if board[i][j] == word[0]:
#                     start.append([i, j])

#         def dfs(ans, idx, column, row):
#             nonlocal answer, visited
#             if ans == word:
#                 answer = True
#             if idx > len(word)-1 or column < 0 or column > len(board) - 1 or row < 0 or row > len(board[0]) - 1:
#                 return

#             if (column+1, row) not in visited and column+1 <= len(board) - 1 and board[column+1][row] == word[idx]:
#                 visited.add((column+1, row))
#                 dfs(ans+board[column+1][row], idx+1, column+1, row)
#             if (column-1, row) not in visited and column - 1 >= 0 and board[column - 1][row] == word[idx]:
#                 visited.add((column-1, row))
#                 dfs(ans+board[column-1][row], idx+1, column-1, row)
#             if (column, row+1) not in visited and row+1 <= len(board[0]) - 1 and board[column][row+1] == word[idx]:
#                 visited.add((column, row+1))
#                 dfs(ans+board[column][row+1], idx+1, column, row+1)
#             if (column, row-1) not in visited and row-1 >= 0 and board[column][row-1] == word[idx]:
#                 visited.add((column, row-1))
#                 dfs(ans+board[column][row-1], idx+1, column, row-1)

#         answer = False
#         for i2, j2 in start:
#             ans = board[i2][j2]
#             idx = 1
#             column = i2
#             row = j2
#             visited = set()

#             dfs(ans, idx, column, row)

#         return answer
