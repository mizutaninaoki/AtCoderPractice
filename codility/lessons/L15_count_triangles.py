# 自分の解答(尺取り法使用)
# 45%
def solution(A):
    if len(A) <= 2:
        return 0

    A = sorted(A)
    # 配列の準備（R は 0 番目から始まることに注意）
    R = [0] * len(A)

    # しゃくとり法
    prev = -1
    for i in range(0, len(A)-2):
        # スタート地点を決める
        if i == 0:
            R[i] = 0
        else:
            R[i] = R[i - 1]  # １つ前の位置の値を初期値に設定

        # ギリギリまで増やしていく(１つずつRの配列の地点を前に進めて、尺取りの元と先端部分の値が10(K)以下でないかチェックして、OKだったら、尺を１つ先に進めて再度チェックする)
        idx = i
        while idx < len(A)-2:
            if A[i] != prev and A[i] + A[idx+1] > A[idx+2]:
                R[i] += len(A[idx+2:])
            idx += 1
        prev = A[i]

    return R[-3]

# see: https://app.codility.com/programmers/lessons/15-caterpillar_method/count_triangles/
# 100%
# https://zenn.dev/paraches/articles/codility_lesson_9_16#%E5%95%8F%E9%A1%8C-7


def solution(A):
    sorted_a = sorted(A)  # 昇順にソート
    count = 0

    # iには大きいインデックスの値が順番に渡ってくる(４つの要素を持つ配列の場合、iには3,2,1,0の順で渡ってくる)
    for i in reversed(range(len(A))):
        min_index = 0
        second_index = i - 1  # ２番目に大きい値のインデックス

        while min_index < second_index:
            # 一番小さい値 + ２番目に小さい値 > 一番大きい値(３角形の成立条件)
            if sorted_a[min_index] + sorted_a[second_index] > sorted_a[i]:
                # この時点で一番小さい値であるmin_index(sorted_a[min_index])をこれ以上大きくしても３角形が成立することがわかっているため、その分(second_index - min_index)を全て足し合わせる
                # ２番目に大きいインデックスからmin_indexを引いた数が
                count += second_index - min_index
                second_index -= 1
            else:
                # min_indexを1ずつ大きくして、sorted_a[min_index]の値を大きくして試していく
                min_index += 1

    return count
