# see: https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_slice_sum/
# 100%(値には−2,147,483,648まで入る可能性があったので、初期値に-infを設定したことがポイント)
def solution(A):
    if len(A) == 0:
        return 0

    tmp_max = float("-inf")
    ans = float("-inf")
    for i in A:
        tmp_max = max(i, tmp_max + i)
        ans = max(ans, tmp_max)
    return ans