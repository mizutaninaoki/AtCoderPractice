# 自分の答え(53%)
def solution(A):
    ans = float("inf")
    for i in range(1, len(A)):
        ans = min(ans, abs(sum(A[:i]) - sum(A[i:])))
    return ans


# 自分の解答２(84%、配列の中が２つの時、なぜか間違った答えを返すっぽい)
# 「全体の合計 - 右側の合計 = 左側の合計」
def solution(A):
    ans = float("inf")
    total = sum(A)
    left = 0

    for i in A:
        left += i
        right = total - left
        ans = min(ans, abs(left - right))
    return ans

# 他者の答え(100%)


def solution(A: [int]) -> int:
    a_sum = sum(A)
    min_delta = 2000

    left_sum = 0
    for i in A:
        left_sum += i
        right_sum = a_sum - left_sum
        delta = abs(left_sum - right_sum)
        if delta < min_delta:
            min_delta = delta

    return min_delta
