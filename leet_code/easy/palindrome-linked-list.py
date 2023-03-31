class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        slow = fast = head
        reversed_list = None

        # 検索中にリストの左半分を反転させる
        # 右半分の始点
        while fast is not None and fast.next is not None:
            tmp = slow

            # keep moving guys
            slow = slow.next
            fast = fast.next.next

            # place node at the start of the reversed half
            tmp.next = reversed_list
            reversed_list = tmp

        # if there are even number of elements in the list
        # do one more step to reach the first element of
        # the second list's half
        # リスト内の要素が偶数個ある場合、最初の要素に到達するために、もう1つのステップを行う。
        # 2番目のリストの半分
        if fast is not None:
            slow = slow.next

        # compare reversed left half with the original
        # right half
        while reversed_list is not None and reversed_list.val == slow.val:
            reversed_list = reversed_list.next
            slow = slow.next

        return reversed_list is None


# 自分で考えた解答。WAだった。。
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         prev = None
#         curr = head

#         while curr:
#             next = curr.next
#             curr.next = prev
#             prev = curr
#             curr = next

#         print(head)
#         print(prev)
#         if head == prev:
#             return True
#         return False
