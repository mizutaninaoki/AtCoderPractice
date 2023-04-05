# 100%
def solution(X, A):
    d = {}
    for idx, i in enumerate(A):
        d[i] = True
        if len(d) == X and all(d):
            return idx
    return -1


# 他者の答え(setを使う方法)
def solution(X: int, A: [int]) -> int:
    pool = set()

    for i, v in enumerate(A):
        pool.add(v)
        if len(pool) == X:
            return i

    return -1
