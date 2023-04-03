# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 最初にノードの深さを数えてから、中央のノードまで進めるやり方(自分の解答)
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        for i in range(length // 2):
            head = head.next
        return head

# node.nextとnode.next.nextを使う方法


class Solution(object):
    def middleNode(self, head):
        # While slow moves one step forward, fast moves two steps forward.
        # Finally, when fast reaches the end, slow happens to be in the middle of the linked list.
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
