# 自分の解答(100%、enumerate使った方法。最初にAがからの時の場合分けをしなくてはいけないから、あまり良いコードじゃないかも)
def solution(A):
    if len(A) == 0:
        return 1
    A = sorted(A)
    for idx, i in enumerate(A):
        if idx + 1 != i:
            return idx + 1
    return A[-1] + 1


# 他者のコード(100%)
def solution(A: [int]) -> int:
    A.sort()

    for i in range(len(A)):
        if i + 1 != A[i]:
            return i + 1

    return len(A) + 1
