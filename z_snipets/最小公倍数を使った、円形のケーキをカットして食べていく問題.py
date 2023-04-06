# see: https://app.codility.com/programmers/lessons/12-euclidean_algorithm/chocolates_by_numbers/
# 100%(最小公倍数を使う)
import math


def solution(N, M):
    # math.gcdで最大公約数を算出して、その値で最小公倍数を算出して、Mで割っている。
    least_common_multiple = N * M // math.gcd(N, M)
    return least_common_multiple // M


# 100% math.gcdを使わないやり方
# 最大公約数はユークリッドの互助法で求められる。
def solution(N, M):
    least_common_multiple = N * M // GCD(N, M)
    return least_common_multiple // M

# ユーグリッドの互除方


def GCD(A, B):
	while A >= 1 and B >= 1:
		if A >= B:
			A = A % B  # A の値を変更する場合
		else:
			B = B % A  # B の値を変更する場合
	if A >= 1:
		return A
	return B
