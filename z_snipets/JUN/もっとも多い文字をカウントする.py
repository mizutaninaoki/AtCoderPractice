"""
Input: "This is a pen. This is an apple. Applepen."
Output: ('p', 6)
"""

import operator
from collections import Counter
from typing import Tuple

# Inputの文字を小文字に直して、その中で一番出現回数が多い文字を取得する

# 配列を使う場合


def count_chars_v1(strings: str) -> Tuple[str, int]:
    strings = strings.lower()
    l = []
    for char in strings:
        # 空文字は飛ばす
        if not char.isspace():
            l.append((char, strings.count(char)))
    return max(l, key=operator.itemgetter(1))

# 辞書を使う場合


def count_chars_v2(strings: str) -> Tuple[str, int]:
    strings = strings.lower()
    d = {}
    for char in strings:
        if not char.isspace():
            d[char] = d.get(char, 0) + 1
    max_key = max(d, key=d.get)
    return max_key, d[max_key]

# Counterを使う場合


def count_chars_v3(strings: str) -> Tuple[str, int]:
    strings = strings.lower()
    d = Counter()
    for char in strings:
        if not char.isspace():
            d[char] += 1
    max_key = max(d, key=d.get)
    return max_key, d[max_key]


if __name__ == "__main__":
    s = "This is a pen. This is an apple. Applepen."
    print(count_chars_v1(s))
    print(count_chars_v2(s))
    print(count_chars_v3(s))
