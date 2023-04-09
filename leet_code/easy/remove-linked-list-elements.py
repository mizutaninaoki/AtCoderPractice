# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 自分の解答。次のノードと今のノードの値を比較する方法
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head

        ans = root = ListNode(head.val)

        # 次のノードが指定された値(val)を持つノードであれば、次の次のノードに入れ替える。次の次のノードがなければ、Noneにする。
        while head.next:
            if head.next.val == val:
                head.next = head.next.next if head.next.next else None
                continue

            root.next = head.next  # ここでrootのnextを更新。つまり、ポインタで連動してansの値も更新される。
            head = head.next  # headを次に進める
            root = root.next  # rootを次に進める

        # 最初のノードが指定された値(val)を持つノードである可能性があるため、チェック。
        # 指定された値(val)を持つノードであれば、次のノードを一番目と入れ替える。
        if ans.val == val:
            ans = ans.next
        return ans


# 他者の解答
class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        dummy_head = ListNode(-1)
        dummy_head.next = head

        current_node = dummy_head
        while current_node.next != None:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next

        return dummy_head.next
