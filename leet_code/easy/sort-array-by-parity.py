# 自分の解答
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        from collections import deque
        que = deque()
        # 偶数であれば先頭に追加して、奇数であれば末尾に追加する
        for i in nums:
            if i % 2 == 0:
                que.appendleft(i)
            else:
                que.append(i)
        return que

# sortのキーを使ってone lineで書く方法


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return sorted(A, key=lambda x: x % 2)
