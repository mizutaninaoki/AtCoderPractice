from functools import reduce
from operator import mul

# 44%
def solution(A):
    maxes = sorted(A)[-3:]
    return reduce(mul, maxes)

# 100%
def solution(A):
    A.sort()
    N = len(A)
    p1 = A[N-1]*A[0]*A[1]  # ソートした配列の中で、絶対値が一番大きい要素が２つ負の値だった時、最大になる
    p2 = A[N-1]*A[N-2]*A[N-3]  # 上記以外の場合、配列の最後３つの値を乗算したものが最大になる
    return max(p1, p2)
