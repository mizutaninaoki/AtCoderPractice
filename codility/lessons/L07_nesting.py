# 100%
def solution(S):
    stack = []
    for s in S:
        if s == "(":
            stack.append(")")
        elif len(stack) != 0 and s == ")":
            stack.pop()
        elif len(stack) == 0 and s == ")":
            return 0

    if len(stack) != 0:
        return 0
    return 1
