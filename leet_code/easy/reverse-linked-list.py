# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            # 次のnodeを一旦nextに代入して待避
            next = curr.next
            # currの先頭のnodeだけ残して、curr.nextには過去のnodeを入れる。(先頭だけ残して、それ以外は過去(prev)で入れ替えるイメージ。それをnodeの数だけ繰り返している)
            curr.next = prev

            # ループするごとに以下のようにprevは変化していく
            # ListNode{val: 1, next: None}
            # ListNode{val: 2, next: ListNode{val: 1, next: None}}
            # ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}
            prev = curr # このcurrには「今到達している先頭のnode + nextには今までのnode(prev)」が入っている
            # currを１つ次へ移動して、次のループで「先頭のval + prev(nextの値)」の形にもってこれるようにする
            curr = next
        return prev       # prevの中には、結果的に逆順の連結リストが入っている