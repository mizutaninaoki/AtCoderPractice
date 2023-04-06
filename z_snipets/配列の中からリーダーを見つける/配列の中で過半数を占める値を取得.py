# see: https://app.codility.com/programmers/lessons/8-leader/dominator/
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
