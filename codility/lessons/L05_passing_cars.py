# 50%
def solution(A):
    pairs = 0
    for idx, i in enumerate(A):
        if i == 0:
            pairs += sum(A[idx+1:])
    return pairs


# 70%
def solution(A):
    pair = 0
    a_sum = sum(A)
    for idx, i in enumerate(A):
        if i == 0:
            pair += a_sum
        else:
            a_sum -= 1
    return pair


def solution(A: [int]) -> int:
    east_car = 0
    passing = 0

    for i in A:
        if i == 1:
            # 今まで保存した東に向かう車の数だけ増やす
            passing += east_car
        else:
            east_car += 1

    # 1000000000台以上すれ違ったら、-1を返すようにする
    if passing > 1000000000:
        passing = -1

    return passing
