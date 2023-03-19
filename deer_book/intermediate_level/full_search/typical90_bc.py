# --------------------
# 自分の解法(TLE)
# --------------------
# from functools import reduce
# import operator
# import itertools
# n, p, q = map(int, input().split())
# L = list(map(int, input().split()))
# c = itertools.permutations(L, 5)

# cnt = 0
# for v in c:
#     if reduce(operator.mul, v) % p == q:
#         cnt += 1
# print(cnt)


# 1点注意したいのが、P で割るとQ 余ること確認する際、組み合わせの整数をa,b,c,d,eとして
# (a*b*c*d*e)%P==Qを実行しようとすると、計算の桁が大きくなることで処理に時間がかかり、TLEとなってしまう点です。

# ですので、計算途中で桁が大きくなりすぎないように
# a % P * b % P * c % P * d % P * e % P == Q で実行します。※上記の式と結果は同じです。

# ------------------------------------------------------------------------------------------------------------
# それぞれの値をまとめて乗算してからある数で割った余りと、それぞれの数を乗算して割った余りを繰り返した、最終的なあまりは同じ。
# 大きな桁数の計算は非常に時間がかかるため、計算途中も小さい数に抑えた方が早くなる！
# ------------------------------------------------------------------------------------------------------------
# print((1 * 2 * 3 * 4 * 5) % 7)
# 1
# print(1 * 2 % 7 * 3 % 7 * 4 % 7 * 5 % 7)
# 1

# --------------------
# 他者の解法(その１)
# --------------------
import sys
from itertools import combinations
n, p, q = map(int, input().split())
L = list(map(int, input().split()))

cnt = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            for l in range(k+1, n):
                for m in range(l+1, n):
                    if L[i] * L[j] % p * L[k] % p * L[l] % p * L[m] % p == q:
                        cnt += 1
print(cnt)


# ------------------------------------------
# 他者の解法(その２)　combination使う方法
# ------------------------------------------
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

N, P, Q = map(int, input().split(" "))
nums = list(map(int, input().split(" ")))

ans = 0
combs = combinations(nums, 5)
for a, b, c, d, e in combs:
    if a % P * b % P * c % P * d % P * e % P == Q:  # (a*b*c*d*e)%PだとTLEになる
        ans += 1

print(ans)
