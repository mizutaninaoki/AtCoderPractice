"""
Input: {'key1': 'value1', 'key2': [1,2,3], 'key3': (1,2,3)} Output: True
Input: {'key1: ['value1', 'key2': [1,2,3], 'key3': (1,2,3)} Output: False
"""


def validate_format(chars: str) -> bool:
    lookup = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for char in chars:
        # 最初に定義したlookupのkeyの中にある文字が来た場合、stackに追加する
        if char in lookup.keys():
            # キーに対応した、閉じる側のカッコをstackに追加
            stack.append(lookup[char])

        # charの文字閉じる側のカッコだった場合、ちゃんとstackの一番上の閉じるカッコの種類が同じかどうかチェック
        if char in lookup.values():
            if not stack:
                return False
            # pop()でstackの一番上の要素を取り出して削除。ちゃんと対応したカッコかどうかチェック。
            if char != stack.pop():
                return False

    # 開く側のカッコに対応した閉じる側のカッコのチェックは上の段階で全て、完了。あとは文字列の最後に閉じる側のカッコが存在するパターンもあるため、
    # ここでstackをチェックして、stackに値が残っていたらFalse。
    if stack:
        return False

    return True


if __name__ == '__main__':
    j = "]{'key1': 'value1', 'key2': [1,2,3], 'key3': (1,2,3)}"
    print(validate_format(j))
