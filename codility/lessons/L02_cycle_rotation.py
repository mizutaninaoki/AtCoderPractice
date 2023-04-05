# 自分の解答(100%)
def solution(A, K):
    length = len(A)
    if length == 0:
        return A
    # 配列Aの長さ分roteteすると元に戻るため、その分はあらかじめ移動させないようにする
    move = K - (length * (K // length))
    return A[-move:] + A[:-move]


# 余りを使った方法(100%)
def solution(A: [int], K: int) -> [int]:
    a_length = len(A)
    if a_length == 0 or K == 0:
        return A

    k = K % a_length
    if k == 0:
        return A

    right_array = A[:a_length - k]
    left_array = A[-k:]

    return left_array + right_array
