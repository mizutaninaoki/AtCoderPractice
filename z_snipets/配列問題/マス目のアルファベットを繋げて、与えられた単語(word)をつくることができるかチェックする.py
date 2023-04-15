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
