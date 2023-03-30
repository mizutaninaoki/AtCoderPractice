# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next # nextはポインタです。
from itertools import zip_longest

# ListNodeは連結リスト
# see: https://qiita.com/tsudaryo1715/items/12c4848028716ab015bb


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 or list2
        if list1.val >= list2.val:
            # リスト１の値の方が大きい場合、リスト２
            # nextの値を変える -> ポインタに新しい値を代入することになるため、この時list2のnextの値も書き換えられる
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        else:
            list1.next = self.mergeTwoLists(list2, list1.next)
            return list1

# singly-linked listについて
# https://astrostory.hatenablog.com/entry/2020/02/24/070213


# -------------
# 他の解答1
# -------------
class Solution:
    def mergeTwoLists(self, a, b):
        if a and b:
            if a.val > b.val:
                a, b = b, a
            a.next = self.mergeTwoLists(a.next, b)
        return a or b


# -------------
# 他の解答2
# -------------
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # tempとansにListNodeクラスのvalに0を入れて初期化（以下）
        # ListNode{val: 0, next: None}
        # 通常であればtempとansの値をそれぞれ書き換えても、お互いの値をどちらもへんこうしてしまうようなことはpythonでは起こらないが、連結リストの場合、nextには次のノードへのポインタが
        # 入っているため、ansを変更するとtempも一緒に変更されるようになっている。
        temp = ans = ListNode(0)
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    # nextの値を変える -> ポインタに新しい値を代入することになるため、この時tempのnextの値も書き換えられる
                    # イメージとしては、ans.nextに代入しながら、その時に最小値をtempに都度入れていっている感じ
                    ans.next = l1
                    l1 = l1.next
                else:
                    ans.next = l2
                    l2 = l2.next
            elif l1:
                ans.next = l1
                l1 = l1.next
            elif l2:
                ans.next = l2
                l2 = l2.next
            # この時は、ans.nextの値を新しくansという変数に格納しているだけであるため、tempの値は全く変更されない。(tempの値が変わるのは、ans.next = 〇〇の時だけ)
            ans = ans.next
        return temp.next


# -------------
# 他の解答3(これが一番わかりやすいかも)
# -------------
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = ListNode(0)
        ans = cur

        while (list1 and list2):
            if (list1.val > list2.val):
                cur.next = list2
                list2 = list2.next
            else:
                cur.next = list1
                list1 = list1.next

            cur = cur.next

        while (list1):
            cur.next = list1
            list1 = list1.next
            cur = cur.next

        while (list2):
            cur.next = list2
            list2 = list2.next
            cur = cur.next

        return ans.next
