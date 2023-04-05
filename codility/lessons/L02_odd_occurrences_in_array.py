# 自分の解答(Counterを使う。100%)
def solution(A):
    from collections import Counter
    counter = Counter(A)
    for k, v in counter.items():
        # 余りが0でない場合は奇数
        if v % 2 != 0:
            return k

# 他者の解答(setを使う。100%)


def solution(A):
    pool = set()
    for i in A:
        if i in pool:
            pool.remove(i)
        else:
            pool.add(i)
    return pool.pop()
