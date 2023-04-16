# 他者の解答(再帰を利用して、マージソートのような形でソートを行っている)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head、もしくは次のheadがNoneであれば現在のheadを返す
        if not head or not head.next:
            return head
        # 現在のheadをslow、次のheadをfastとする。
        slow, fast = head, head.next
        # fast or fast.nextがNoneになるまで、slowとfastを右に進めていく
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # startを現在のslowの次のnodeに、slow.nextはNoneを入れて、
        start = slow.next
        slow.next = None
        # lからrまでのノードをmerge()で新しくソート順に生成しながらノードツリーを作る。
        # マージソートの要領でリストを真ん中より左と右に分けて、ソートしていっている。
        l, r = self.sortList(head), self.sortList(start)
        return self.merge(l, r)
        
        
    def merge(self, l, r):
        if not l or not r:
            return l or r
        dummy = p = ListNode(0)
        # lもしくはrどちらかがなくなるまで、lとrのうち、小さい方をp.nextに入れていく。小さい値を入れたら、その小さいl、もしくはrの次(l.next or r.next)をpにして、
        # 進めていき、dummyに小さいvalを持つノード順にソートされたノードツリーが作られるようにする。
        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
            else:
                p.next = r
                r = r.next
            p = p.next
        p.next = l or r
        # 最初のノードにはListNode(0)の時の0をnode.valに持つノードが存在するため、dummy.nextを返すようにする。
        return dummy.next
            