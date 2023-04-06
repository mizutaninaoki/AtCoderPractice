# 最大公約数は以下で求められる。(ユーグリッドの互除法)
import math


def GCD(A, B):
	while A >= 1 and B >= 1:
		if A >= B:
			A = A % B  # A の値を変更する場合
		else:
			B = B % A  # B の値を変更する場合
	if A >= 1:
		return A
	return B


# ユーグリッドの互除法を使わず、pythonのライブラリ(math.gcd)でも最大公約数を求めることはできる。
math.gcd(A, B)
