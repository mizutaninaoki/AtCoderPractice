# 自分の解答。TLEになる。
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#         headB_tmp = headB
#         while headA:
#             if not headA or not headB:
#                 return None

#             while headB_tmp:
#                 if headA == headB_tmp:
#                     return headA
#                 headB_tmp = headB_tmp.next
#             headB_tmp = headB
#             headA = headA.next
#         return None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None

        pa = headA
        pb = headB

        # headA(pa)とheadB(pa)を1つずつnextに遷移させて比較していく。
        # headA、headB、最後まで到達したら、それぞれのポインタをテレコ（headA->headB、headB->headA）にして再度探索する。
        # これによって、ノード数が違う場合でも、たとえばノード数が１つ違う場合は、１つづつ比較するノードがずれつつ、比較できるようになる。
        # どちらも最後尾のノードでNoneになった時は、全ての組み合わせが完了してどちらもNoneになった時だから、whileループを抜けて、
        # その時のpaの値であるNoneが返される
        while pa is not pb:
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next
        return pa
