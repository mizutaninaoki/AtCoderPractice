# 100%
def solution(A):
    A.sort()
    for i in range(0, len(A)-2):
        if A[i] <= 1:
            continue

        if A[i] + A[i+1] > A[i+2]:
            return 1
    return 0

# 他者の解答(100%)
# ソートして順番にA[P]+A[Q]>A[R]が成り立つかどうかを調べれば良い。
# 因みに、3つの数字のうちどれか一つ以上がマイナスの値になると式は成り立たない。今回Aに含まれる要素にはマイナスの値も入っているので、スピードアップの為に大きい数から調べて行って、マイナスの値が出てきたら処理を切り上げて0を返す。


def solution(A: [int]) -> int:
    if len(A) < 3:
        return 0

    A.sort()

    for i in reversed(range(2, len(A))):
        pv = A[i-2]
        qv = A[i-1]
        rv = A[i]

        if pv < 0:
            return 0

        if pv + qv > rv:
            return 1

    return 0
