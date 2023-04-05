def solution(X, Y, D):
    distance = Y - X
    jumps = distance // D
    mod_distance = distance % D
    return jumps + 1 if mod_distance else jumps
