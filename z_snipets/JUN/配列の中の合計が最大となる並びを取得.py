"""
1, 配列の中で合計が最大となる並びを抜き出す
Input [1, -2, 3, 6, -1, 2, 4, -5, 2]
Output 14 (3, 6, -1, 2, 4)

２, 配列の中で合計が最大となる並びを抜き出す（循環OK。最後から最初に戻って連続してもよい） -> つまり、配列の中で最もマイナスとなる（最小となる）並びを除外したものを抜き出せば良い
Input [1, -2, 3, 6, -1, 2, 4, -5, 2]
Output 14 (3, 6, -1, 2, 4)
"""

from typing import List

# 1の解き方


def get_max_min_sequence_sum(numbers: List[int], operator=max) -> int:
    result_sequence, sum_sequence = 0, 0
    for num in numbers:
        # 今回の値(num)+今までの合計が今回の値(num)より大きければsum_sequenceに上書き。
        # 小さければ、ここで今までの合計をリセットして、sum_sequenceには今回の値(num)を代入する
        sum_sequence = operator(num, sum_sequence + num)
        # 今までの並びの合計の最大値(result_sequence)と、今回までの並びの最大値(sum_sequence)を比較して、大きい方をresult_sequenceに代入する。
        result_sequence = operator(result_sequence, sum_sequence)
    return result_sequence

# 2の解き方


def find_max_circulator_sequence_sum(numbers: List[int]) -> int:
    max_sequence_sum = get_max_min_sequence_sum(numbers)
    # 「配列の中で最もマイナスとなる（最小となる）並び」から全体の合計を引けば、配列の中の最大となる並びの合計値を算出できる
    max_wrap_sequence = sum(numbers) - \
        get_max_min_sequence_sum(numbers, operator=min)
    return max(max_sequence_sum, max_wrap_sequence)


if __name__ == "__main__":
    print(get_max_min_sequence_sum([1, -2, 3, 6, -1, 2, 4, -5, 2]))
    print(find_max_circulator_sequence_sum([1, -2, 3, 6, -1, 2, 4, -5, 2]))
