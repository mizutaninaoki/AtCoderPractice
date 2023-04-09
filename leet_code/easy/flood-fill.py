# 自分の解答。(stackを使ったDFS。再帰が永久ループしてしまう。。。)
# class Solution:
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

#         stack = [(sr, sc)]
#         base_color = image[sr][sc]
#         row_len = len(image[0])
#         col_len = len(image)

#         while stack:
#             r, c = stack.pop()

#             # 上
#             if 0 <= r-1 and image[r-1][c] == base_color:
#                 image[r-1][c] = color
#                 stack.append((r-1, c))
#             # 右
#             if c+1 < row_len and image[r][c+1] == base_color:
#                 image[r][c+1] = color
#                 stack.append((r, c+1))      
#             # 下
#             if r+1 < col_len and image[r+1][c] == base_color:
#                 image[r+1][c] = color
#                 stack.append((r+1, c))    
#             # 左
#             if 0 <= c-1 and image[r][c-1] == base_color:
#                 image[r][c-1] = color
#                 stack.append((r, c-1))   

#         image[sr][sc] = color
#         return image
    
    
# 再帰を使ったDFS
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        color_to_change = image[sr][sc]
        
        def dfs(r, c):
            # 関数の外にある rows, cols, newColor, image を更新したいので nonlocal 宣言をする
            nonlocal rows, cols, newColor, image
            
            # はみ出ている場合、すでにnew_colorに変わっている場合、変えるのに指定された色(color_to_change)で無い場合はreturn
            if r < 0 or c < 0 or r>rows-1 or c>cols-1 or image[r][c]==newColor or image[r][c]!=color_to_change:
                return
            
            # 「上の条件に当てはまらない　== 色を変えるマスである」ということなので、色を変える
            image[r][c] = newColor
            
			# radiate in four directions(下、上、右、左を再度DFSで探索する)
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        dfs(sr, sc)
        
        return image