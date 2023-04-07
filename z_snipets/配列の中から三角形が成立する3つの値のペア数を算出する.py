# see: https://app.codility.com/programmers/lessons/15-caterpillar_method/count_triangles/
# 100%
# https://zenn.dev/paraches/articles/codility_lesson_9_16#absdistinct
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
