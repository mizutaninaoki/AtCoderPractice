import unittest
import math
import time


def is_prime_v1(num: int) -> bool:
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def is_prime_v2(num: int) -> bool:
    if num <= 1:
        return False

    # 調べたい数字(num)のルートを取った整数値 + 1までで、２で割った時あまりがでなければ素数
    for i in range(2, math.floor(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


# numが２瀬あった時と、二の倍数(素数ではない)をあらかじめループの中のチェック対象から排除することで、速度を上げたやりかた
def is_prime_v3(num: int) -> bool:
    if num <= 1:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    # 2飛ばしでチェック
    for i in range(3, math.floor(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


# ファイル名を日本語にしてて、メソッドが別ファイルで読み込めないので、仕方なく同じファイルにテストケース書く。


class PrimeTest(unittest.TestCase):

    def test_is_prime_ok(self):
        for i in [2, 3, 5, 7, 11, 13, 17, 19]:
            self.assertTrue(is_prime_v3(i))

    def test_is_prime_no(self):
        for i in [1, 4, 6, 8, 9, 10]:
            self.assertFalse(is_prime_v1(i))

    def test_is_prime_negative(self):
        self.assertFalse(is_prime_v1(-1))

    def test_is_prime_typeerror(self):
        with self.assertRaises(TypeError):
            is_prime_v1('string')


if __name__ == '__main__':
    import random
    numbers = [random.randint(0, 1000) for _ in range(100000)]
    start = time.time()
    for num in numbers:
        is_prime_v1(num)
    print("v1", time.time() - start)
    
    start = time.time()
    for num in numbers:
        is_prime_v2(num)
    print("v2", time.time() - start)
    
    start = time.time()
    for num in numbers:
        is_prime_v3(num)
    print("v3", time.time() - start)
    # unittest.main()はモジュール内の全てのtest_xxxメソッドを呼び出して実行する役割
    # unittest.main()
