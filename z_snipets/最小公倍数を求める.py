# 100% math.gcdを使わないやり方
# 最大公約数はユークリッドの互助法で求められる。
import math


def least_common_multiple(N, M):
    # least_common_multipleには最小公倍数が入る。最小公倍数は最大公約数を使って算出する。
    least_common_multiple = N * M // GCD(N, M)
    # math.gcdを使っても最小公倍数を３種流することができる
    least_common_multiple = N * M // math.gcd(N, M)

# ユーグリッドの互除方(GCD)


def GCD(A, B):
	while A >= 1 and B >= 1:
		if A >= B:
			A = A % B  # A の値を変更する場合
		else:
			B = B % A  # B の値を変更する場合
	if A >= 1:
		return A
	return B
