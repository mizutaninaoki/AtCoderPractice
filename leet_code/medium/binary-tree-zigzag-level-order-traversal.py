# 他者の回答(DFS)
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        def dfs(node, depth):
            if node:
                # ansに深さ分(depth)のリストが存在しない場合は空のリストを入れておいて、ans[depth].append(node.val)でエラーにならないようにする。
                if len(ans) <= depth:
                    ans.append([])
                # 現在の深さ(depth)に対応するansの中のリストに、node.valを追加する
                ans[depth].append(node.val)
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)
        dfs(root, 0)
        # 深さが奇数の場合、リストを逆順(右のノード->左のノード)にする。深さが偶数の場合は、通常のまま。
        return [ans[i] if i%2==0 else ans[i][::-1] for i in range(len(ans))]
    
    
# 自分の解答(DFS+deque(リストの中を逆順にしたいから。BFSは使ってない))
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        def dfs(node, depth):
            nonlocal ans
            if not node:
                return
            
            if len(ans)-1 < depth:
                ans.append(deque())
            # 深さが奇数の場合、リストを逆順(右のノード->左のノード)にしたいため、dequeのリストにappendleft()で先頭から追加していく。
            # 深さが偶数の場合は、通常のままappend()で最後から追加していく。
            if depth % 2 == 0:
                ans[depth].append(node.val)
            else:
                ans[depth].appendleft(node.val)

            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        
        from collections import deque
        ans = []
        dfs(root, 0)
        return ans