s = "test"

# 以下２つの書き方でも簡単に回文かどうかを調べることはできる
s == "".join(reversed(s))
s == s[::-1]

# 以下は上の２つのやり方以外の、python固有のメソッド等を使わず、アルゴリズムで解く方法

"""
1, Check Palindrome
aba => True
abc => False
racecar => True

2, Find Palindrome
abcracecarbda => cec, aceca, racecar
"""

# 上の例の１の方の答え
# 両端から１文字ずつ同じかどうかチェック。全て同じで回文になっていたら、Trueを返す。


def is_palindrome(strings: str) -> bool:
    len_strings = len(strings)
    # 空文字の時
    if not len_strings:
        return False
    # １文字の時
    if len_strings == 1:
        return True

    start, end = 0, len_strings - 1
    # 両端から同じ文字かチェック。
    while start < end:
        if strings[start] != strings[end]:
            return False
        start += 1
        end -= 1
    return True

# 上の例の２の方の答え(文字列の中に潜む部分的な回文の文字列を取得する)

# 文字列の両端から１文字ずつ取得アンド比較して、同じであれば部分的に回文になっているので、resultのリストに追加する


def find_palindrome(strings: str, left: int, right: int):
    result = []
    while 0 <= left and right <= len(strings) - 1:
        if strings[left] != strings[right]:
            break
        result.append(strings[left:right+1])
        left -= 1  # 対象の文字から左に１文字分ずずらして、右の文字と比較
        right += 1  # 対象の文字から右に１文字分ずずらして、左の文字と比較
    return result

# 文字列を１文字ずつ進めて、文字列の中に回文がないかチェックしていく


def find_all_palindrome(strings: str):
    result = []
    len_strings = len(strings)
    if not len_strings:
        return result
    if len_strings == 1:
        result.append(strings)

    # １文字ずつ進めて、両隣の文字列が同じかチェックして、部分回文でないかチェックする
    for i in range(1, len_strings - 1):
        [result.append(s) for s in find_palindrome(
            strings, i-1, i+1)]  # aba のような奇数文字列
        [result.append(s) for s in find_palindrome(
            strings, i-1, i)]  # abbaのような偶数文字列
    return result


if __name__ == "__main__":
    print(find_all_palindrome('adsfdafracecardfdsfdsf'))
