# see: https://leetcode.com/problems/middle-of-the-linked-list/description/
# node.nextとnode.next.nextを使う方法
class Solution(object):
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # While slow moves one step forward, fast moves two steps forward.
        # Finally, when fast reaches the end, slow happens to be in the middle of the linked list.
        # slowが1歩進む間に、fastは2歩進む。
        # 最後にfastが終点に到達したとき、slowは偶然にもリンクリストの真ん中にいることになる。
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
