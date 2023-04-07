# 100%
def solution(A):
    s = set()
    for i in A:
        s.add(abs(i))
    return len(s)
