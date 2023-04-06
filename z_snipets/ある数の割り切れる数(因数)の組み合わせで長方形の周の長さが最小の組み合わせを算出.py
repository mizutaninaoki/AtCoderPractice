# see: https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/min_perimeter_rectangle/
import math


def solution(N):
    # 因数はルートを取った数+1まで調べればOK
    sqrt_num = int(math.sqrt(N))
    ans = float("inf")
    for i in range(1, sqrt_num + 1):
        if N % i == 0:
            ans = min(ans, 2 * (i + N // i))
    return ans
