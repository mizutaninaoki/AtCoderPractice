# see: https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/count_factors/
# 因数を求める。
# 例だと 1, 2, 3, 4, 6, 8, 12, 24で、これは 1x24, 2x12, 3x8, 4x6になる。
# で、因数は片方がわかればもう片方もわかる。例だと1, 2, 3, 4がわかれば残りの4つもわかる。
# ここで、因数の（1x24や2x12などの）組みの小さい方は、Nの平方根よりも小さくなる。
# 例えば36の場合は1, 2, 3, 4, 6が因数の小さい方で、この中で一番大きな6はちょうど36の平方根になる。
# と言うわけで、あとは力技のループでNが割り切れるかどうかを確認する。
import math


def solution(N):
    # 集合を使って、最後にlen()を使わないと、単にカウントするだけでは(余りがゼロの時にプラス2するやり方)、「2x12」の時と、「12x2」で重複分も足し合わせてしまって正しい因数を求めることができない
    factors = {1, N}  # N = 1の時、代入時点で{1, 1}となり、重複しているので、{1}となる
    sqrt_num = int(math.sqrt(N))
    for i in range(2, sqrt_num+1):
        if N % i == 0:
            factors.add(i)
            # 例えば上の例で、i=3の時、ここは24 // 3 = 8が集合(factors)に追加される
            factors.add(N // i)
    return len(factors)
