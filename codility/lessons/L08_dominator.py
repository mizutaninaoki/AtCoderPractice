# 75%(こっちの方が簡潔でわかりやすい)
def solution(A):
    from collections import Counter
    falf = len(A) // 2
    # 奇数であればdominatorは「商+1」になる
    dominator_num = falf if len(A) % 2 == 0 else falf + 1

    counter = Counter(A)
    most_appear_num = max(counter, key=counter.get)
    # 出現回数が全体の要素数の半分未満の場合、−１を返す
    if dominator_num > counter[most_appear_num]:
        return -1

    # 配列の中で過半数を占める数字の最初に出てきたインデックスを返す
    for idx, i in enumerate(A):
        if most_appear_num == i:
            return idx


# 100%だけどわかりにくい
def solution(A: [int]) -> int:
    if len(A) == 0:
        return -1

    a = [(i, v) for i, v in enumerate(A)]
    a.sort(key=lambda x: x[1])

    max_count = 0
    pre_i, pre_v = a[0]
    max_value_index = pre_i

    count = 0
    for i, v in a:
        if v == pre_v:
            count += 1
        else:
            if count > max_count:
                max_count = count
                max_value_index = pre_i
            count = 1
            pre_i, pre_v = i, v

    if count > max_count:
        max_count = count
        max_value_index = pre_i

    return max_value_index if max_count > len(A) / 2 else -1
