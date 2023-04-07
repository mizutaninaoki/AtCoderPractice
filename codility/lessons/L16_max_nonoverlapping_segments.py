# 80%(Timeoutになる)
def solution(A, B):
    if len(A) < 2:
        return len(A)

    cnt = 0
    curr_location = float("-inf")
    for idx, (a, b) in enumerate(zip(A, B)):
        # Aで次に選択できるもの、かつ、あとは貪欲法でとにかくBの位置が最小となるものを選んでいけば、最大の重複しないセグメントの数が数えられる
        if a > curr_location and b == min(B[idx:]):
            curr_location = b
            cnt += 1
    return cnt


# 100%
# 単純に順番に置いた場合に次が置けるかどうか確認する。
# (この問題はBの位置が必ず前のBの位置よりも大きいのが条件にあるため、単純に次が置けるかどうか確認するだけで解が求まる)
def solution(A: [int], B: [int]) -> int:
    if len(A) < 2:
        return len(A)

    count = 1
    end_number = B[0]

    for i in range(len(A)):
        if A[i] > end_number:
            count += 1
            end_number = B[i]

    return count
