# see: https://leetcode.com/problems/validate-stack-sequences/
# 自分の解答
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        tmp = []
        for i in pushed:
            # tmpにpushedの値を追加
            tmp.append(i)

            # tmpの最後に追加された値とpoppedの先頭の値が同じである限り、tmp, popped両方削除していく
            while tmp and tmp[-1] == popped[0]:
                tmp.pop()
                popped.pop(0)
        # 最後にtmpが空のリストであれば、全てpop()出来たということになる
        return len(tmp) == 0


# two pointerを使った解法
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = j = 0
        for x in pushed:
            pushed[i] = x
            while i >= 0 and pushed[i] == popped[j]:
                i, j = i - 1, j + 1
            i += 1
        return i == 0
