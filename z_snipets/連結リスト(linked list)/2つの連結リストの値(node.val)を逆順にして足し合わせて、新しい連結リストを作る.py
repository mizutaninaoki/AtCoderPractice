# see: https://leetcode.com/problems/add-two-numbers/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 自分の解答
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nums_l1 = []
        nums_l2 = []

        # nodeのツリーの最後まで、再帰で探索して、node.valをそれぞれnums_l1、nums_l2に追加していく。
        def dfs(node, nums):
            if not node:
                return

            nums.append(node.val)
            dfs(node.next, nums)
        
        dfs(l1, nums_l1)
        dfs(l2, nums_l2)

        # nums_l1、nums_l2にある配列の値を文字列化して、逆順にしてから足す。
        sum_num = int("".join(map(str, nums_l1[::-1]))) + int("".join(map(str, nums_l2[::-1])))

        ans = tmp = ListNode()
        reversed_s = (str(sum_num))[::-1] # 足し合わせた数を逆順にする
        # 逆順にした数の桁数の値をそれぞれノードに格納していく。
        for i in range(len(reversed_s)):
            tmp.val = int(reversed_s[i])
            # 一番最後のノードには子ノードを作りたくないので、最後だけ飛ばすようにする
            if i < len(reversed_s) - 1:
                tmp.next = ListNode()
                tmp = tmp.next
        
        return ans
    
    
# 他者の解答(carryを使うやり方)
def addTwoNumbers(self, l1, l2):
    dummy = cur = ListNode(0)
    carry = 0
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        cur.next = ListNode(carry%10)
        cur = cur.next
        carry //= 10
    return dummy.next