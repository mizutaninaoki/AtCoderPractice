from typing import List

# 先に偶数だけ集めた配列、奇数だけ集めた配列を用意するやり方


def order_even_first_odd_last_v1(numbers: List[int]) -> None:
    even_list, odd_list = [], []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
    numbers[:] = even_list + odd_list


# 先頭から見ていって、偶数であればそのまま、奇数であれば、配列の最後から順に数字を入れ替えていくやり方
def order_even_first_odd_last_v2(numbers: List[int]) -> None:
    i, j = 0, len(numbers) - 1
    while i < j:
        if numbers[i] % 2 == 0:
            i += 1
        else:
            # 奇数の場合、numbers[i], numbers[j]を入れ替える
            numbers[i], numbers[j] = numbers[j], numbers[i]
            j -= 1


if __name__ == '__main__':
    l = [0, 1, 3, 4, 2, 4, 5, 1, 6, 9, 8]
    order_even_first_odd_last_v2(l)
    print(l)
