# see: https://leetcode.com/problems/linked-list-cycle/
#      https://leetcode.com/problems/linked-list-cycle/solutions/44539/ac-python-76ms-floyd-loop-detection-in-7-lines/
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
