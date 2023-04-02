"""
Input: ["h", "y", "n", "p", "t", "o"], [3, 1, 5, 0, 2, 4]
Output: python
"""

from typing import List


def order_change_indexes_v1(chars: List[str], indexes: List[int]) -> str:
    # charsの文字列分の長さの配列を生成
    tmp = [None] * len(chars)
    # インデックスに対応する数字のアルファベットをtmpに入れていき、joinで文字列に結合
    for i, index in enumerate(indexes):
        tmp[index] = chars[i]
    return "".join(tmp)

# 対応するインデックスが違う場合、入れ替えて試すやり方。（ちょっとややこしいから理解したいのなら、もう一度動画見た方がいいかも）
# https://www.youtube.com/watch?v=jEr95cosRrc&list=PLq-JeSNkOKBRtkNb9QeptJuvE_CwD0NKR&index=8


def order_change_indexes_v2(chars: List[str], indexes: List[int]) -> str:
    i, len_indexes = 0, len(indexes) - 1
    while i < len_indexes:
        while i != indexes[i]:
            index = indexes[i]
            chars[index], chars[i] = chars[i], chars[index]
            indexes[index], indexes[i] = indexes[i], indexes[index]
        i += 1
    return "".join(chars)


if __name__ == "__main__":
    w = ["h", "y", "n", "p", "t", "o"]
    i = [3, 1, 5, 0, 2, 4]
    print(order_change_indexes_v1(w, i))
    print(order_change_indexes_v2(w, i))
