# see: https://leetcode.com/problems/palindrome-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        slow = fast = head
        reversed_list = None

        # 検索中にリストの左半分を反転させる。つまりexample1であれば[1,2,2,1]の最初の２つの[1,2]を逆順にして(reversed_list)、[2,1]にする。
        # その時、slowは右半分の[2,1]を持つ状態になっているため、後の方(２回目の)のwhile内でreverse_listとslowをお互い１つづつnextで進めながら比較していく。

        # example1の時の遷移状況は以下の通り（whileはfastがNoneになっても、while内の一番最後まで到達してからループを抜ける）
        # tmp -> ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}}
        # slow -> ListNode{val: 2, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}
        # fast -> ListNode{val: 2, next: ListNode{val: 1, next: None}}
        # tmp -> ListNode{val: 1, next: None}
        # reversed_list -> ListNode{val: 1, next: None}
        # tmp -> ListNode{val: 2, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}
        # slow -> ListNode{val: 2, next: ListNode{val: 1, next: None}}
        # fast -> None
        # tmp -> ListNode{val: 2, next: ListNode{val: 1, next: None}}
        # reversed_list -> ListNode{val: 2, next: ListNode{val: 1, next: None}}
        while fast is not None and fast.next is not None:
            tmp = slow
            slow = slow.next
            fast = fast.next.next

            # 最初から左半分までのnodeを逆順にしていく
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
        # 左半分（reversed_list。左半分はこの時点でreversed_listに反転した状態になっている）と右半分(slow)を比較
        while reversed_list is not None and reversed_list.val == slow.val:
            reversed_list = reversed_list.next
            slow = slow.next

        return reversed_list is None