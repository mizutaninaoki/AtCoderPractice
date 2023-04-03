"""
1番目は合計値が12となるようなペアを探す。なければ Noneを返す。
1, Input: [11, 2, 5, 9, 10, 3], 12 => Output: (2, 10) or None
2番目は与えられた配列の中から、合計値が同じとなる２つのペアを探す（ペアの個数に制限はないが、配列の中の値全ての使わなければいけない）
2, Input: [11, 2, 5, 9, 10, 3]  => Output: (11, 9) or None ex) 11 + 9 = 2 + 5 + 10 + 3
"""
from typing import List, Tuple, Optional

# 1番目の問の解答(val = target - numでvalを求め、cacheの中を探索していくやり方)


def get_pair(numbers: List[int], target: int) -> Optional[Tuple[int, int]]:
    cache = set()
    for num in numbers:
        cache.add(num)
        # 目的となる値(target)から今引いた数がcacheの中にあれば、その値と今の値(num)を足せば目的の値(target)になるため、ペアを返すようにする
        val = target - num
        if val in cache:
            return val, num


def get_pair_half_sum(numbers: List[int]) -> Optional[Tuple[int, int]]:
    sum_numbers = sum(numbers)
    # 「配列の中の値全ての使わなければいけない」 => 配列の中に負の値がない限り、お互いのペアの合計値は全ての配列の値を２で割った数になるはず（つまり、上の例であれば20(11 + 9)）
    half_sum, remainder = divmod(sum_numbers, 2)
    # ２で割り切れない -> 合計値が等しくなる２つのペアを見つけることはできないため、Falseを返す
    if remainder != 0:
        return False
    
    cache = set()
    for num in numbers:
        cache.add(num)
        # 目的となる値(target)から今引いた数がcacheの中にあれば、その値と今の値(num)を足せば目的の値(target)になるため、ペアを返すようにする
        val = half_sum - num
        if val in cache:
            return val, num
        

if __name__ == "__main__":
    l = [11, 2, 5, 9, 10, 3]
    t = 12
    print(get_pair(l, t))

    l = [11, 2, 5, 9, 10, 3]
    print(get_pair_half_sum(l))