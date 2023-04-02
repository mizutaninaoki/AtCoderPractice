"""
素数生成
Input: 50 => Output: [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
"""

from typing import List

# １ずつ増やして、全探索で素数を生成していく方法


def generate_prime_v1(numbers: int) -> List[int]:
    primes = []
    for x in range(2, numbers + 1):
        for y in range(2, x):
            if x % y == 0:
                break
        else:
            primes.append(x)
    return primes

# エラトステネスのふるいを使った素数生成コード
# cacheという変数に


def generate_prime_v2(numbers: int) -> List[int]:
    primes = []
    cache = {}  # エラトステネスのふるいのために、cacheという変数に素数でないかどうかを記録していく
    for x in range(2, numbers + 1):
        is_prime = cache.get(x)
        # cacheにFalseが入っている数字は、素数ではないことがすでに判明しているため、スキップする
        if is_prime is False:
            continue
        primes.append(x)
        cache[x] = True
        # 今のxの倍数を、飛ばし飛ばしでループを回して、素数ではないためcacheにFalseを入れていく（エラトステネスのふるい）
        for y in range(x*2, numbers + 1, x):
            cache[y] = False
    return primes


if __name__ == "__main__":
    print(generate_prime_v1(50))
    print(generate_prime_v2(50))
