# see: https://app.codility.com/programmers/lessons/8-leader/equi_leader/
# 33%(テストケースが２つ通らない。またタイムアウトテストは全て通らない。)
def solution(A):
    from collections import Counter
    ans = 0
    d = Counter(A)
    equi_leader = max(d, key=d.get)
    prev_left = 0
    for i in range(1, len(A)):
        left = Counter(A[:i])
        # 最大値が同じ出現回数の値がある場合、maxはインデックスが小さいキーを１つだけ返す
        max_left = max(left, key=left.get)
        # 左側の配列数が２以上、かつ集合の要素が1の時([4,4,4]みたいな時)、またはまだ左側にequi_leaderが存在しない場合、スキップ
        if len(A[:i]) >= 2 and len(set(A[:i])) == 1 or max_left != equi_leader:
            continue
        # 左側に最大出現回数が同じ複数要素がある場合、equi_leaderとは認められないから、スキップ
        if len([v for v in left.values() if v >= left[max_left]]) > 1:
            continue

        right = Counter(A[i:])
        max_right = max(right, key=right.get)
        if len(A[i:]) >= 2 and len(set(A[i:])) == 1 or max_right != equi_leader:
            continue
        if len([v for v in right.values() if v >= right[max_right]]) > 1:
            continue

        # 左側のequi_leaderの数が変動したら、ansに1追加して数える
        left_count = A[:i].count(equi_leader)
        if prev_left != left_count:
            prev_left = left_count
            ans += 1
    return ans

# 100%(100%だけど、コードがややこしい)
# https://zenn.dev/paraches/articles/codility_lesson_5_8#equileader


def solution(A: [int]) -> int:
    value_dic = {}
    for i, v in enumerate(A):
        if v in value_dic.keys():
            value_dic[v].append(i)
        else:
            value_dic[v] = [i]

    leader_index_array = max(value_dic.values(), key=lambda x: len(x))
    leader_count = len(leader_index_array)
    equi_leader_count = 0

    index = 0
    left_leader_count = 0
    for leader_index in leader_index_array:
        while index <= leader_index:
            if index == leader_index:
                left_leader_count += 1
            left_size = index + 1
            right_size = len(A) - left_size
            right_leader_count = leader_count - left_leader_count
            if left_leader_count > int(left_size / 2) and right_leader_count > int(right_size / 2):
                equi_leader_count += 1
            index += 1

    return equi_leader_count
