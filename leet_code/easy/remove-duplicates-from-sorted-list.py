# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 自分の解答
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        ans = root = ListNode(head.val)
        stack = set([head.val])

        while head:
            # すでにstackに存在する値であれば、headを次に進ませ、もし最後であればroot.nextに不要なNodeが残ってしまうため、root.nextはNoneにしておく。
            if head.val in stack:
                head = head.next
                root.next = None
                continue
            stack.add(head.val)
            root.next = head
            head = head.next
            root = root.next
        return ans

# 今のnodeと次のnodeの値を比較して進めていく方法


class Solution(object):
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while (temp and temp.next):
            # 現在のvalと次のvalが同じの場合、重複を削除するため、次の次のnodeを次のnodeに代入して、入れ替える
            if (temp.next.val == temp.val):
                temp.next = temp.next.next
                continue
            temp = temp.next
        return head
