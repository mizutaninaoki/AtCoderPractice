# see: https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
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
