# 100%(単純に、順番に紐の長さを足していきKを超えたらカウントしているだけ。Codilityのテストケースが甘い気がする。。。以下URL先の人もおかしさにちょっと疑問を抱いている)
# https://zenn.dev/paraches/articles/codility_lesson_9_16#tieropes
def solution(K, A):
    cnt = 0
    curr_rope = 0

    for a in A:
        curr_rope += a

        if curr_rope >= K:
            cnt += 1
            curr_rope = 0
    return cnt

# see: https://zenn.dev/paraches/articles/codility_lesson_9_16#tieropes
# 他者の解答


def solution(K: int, A: [int]) -> int:
    count = 0
    index = 0
    v_sum = 0

    while index < len(A):
        v_sum += A[index]
        if v_sum >= K:
            count += 1
            v_sum = 0
        index += 1

    return count
