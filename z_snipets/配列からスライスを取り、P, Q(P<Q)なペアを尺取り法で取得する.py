# see: https://app.codility.com/programmers/lessons/15-caterpillar_method/count_distinct_slices/
# 尺取り方を使った解き方(スタート地点(base)から紐(尺)を伸ばして、その間にあるかずだけ数え上げて、紐をいっぱいまで伸ばしたら、それに合わせてスタート地点をずらして、紐を緩ませて、再度測っていくやり方)
def solution(M: int, A: [int]) -> int:
    count = 0  # ペアの数
    index = 0  # 尺の伸ばした先の位置
    base = 0  # 尺の手元の位置(伸ばした先とは逆の位置。尺取りの手元の位置)
    pool = set()  # 尺の中に出現した数を一時的に保管しておく集合

    # 「A[0](base)とA[1](index)」、「A[0](base)とA[2](index)」...のようにbaseを固定して、すでに出現した数字が再度出現するまでindexを進めながら数えていく
    # 尺取りで(A[base], A[index])のような形で進めているため、(P, Q)のような関係性を保ったまま、ペアをカウントすることができる
    while index < len(A):
        # 出現した数字はpoolに一時保管しておく
        # poolにすでに保管している数字がでてきたら、whileを抜ける
        while index < len(A) and A[index] not in pool:
            count += index - base + 1
            pool.add(A[index])
            index += 1

        # baseからその添字の場所までに読んだ数をプールから取り除く。
        # baseの位置もそれに合わせて１ずつ進める
        while index < len(A) and A[base] != A[index]:
            pool.remove(A[base])
            base += 1
        # この時点でpoolには同じだった数のみ残っている。その数を削除して、baseの位置も1ずらして、indexと同じ位置にbaseも持ってきて、再度尺取りをスタートする
        pool.remove(A[base])
        base += 1

    return min(count, 1000000000)
