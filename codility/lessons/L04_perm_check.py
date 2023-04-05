# 100%
def solution(A):
    for idx, i in enumerate(sorted(A)):
        if i != idx + 1:
            return 0
    return 1


