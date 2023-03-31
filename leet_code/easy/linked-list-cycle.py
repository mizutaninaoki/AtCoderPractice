# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 配列を使うやり方の場合、連結リストの最後尾に到達する前に、head.valで同じ値が２回出てくるとそこでTrueを返してしまうようになるため、WAになる。
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         visited = []
#         while head:
#             if head.val in visited:
#                 return True
#             visited.append(head.val)
#             head = head.next
#         return False

# 辞書を使って、連結リストの最後尾に到達する前にhead.valで同じ値が２回出てきても一意のキーにできるようにkeyはheadを使う。
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dictionary = {}
        while head:
            if head in dictionary:
                return True
            # キーにはheadを指定して一意のキーにする。（ただしprintではキーを「Error - Found cycle in the ListNode」が出て、stdoutに出力できないっぽい。）・
            dictionary[head] = True
            head = head.next
        return False


# Two pointers
# 一度に１つ先に進む(slow)ポインターと、一度に２つ先に進む(fast)ポインターを用意して、ポインター(next)が存在するまでずっと進み続ける。
# その際、fastとslowを比較して、循環している状態であれば、いつかfastがslowに１週遅れで追いつくため、その状態になったら循環していることになるためTrueを返す。
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
