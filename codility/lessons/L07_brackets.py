# 100%
def solution(S):
    if len(S) == 0:
        # 空文字が渡ってきた時は、1を返す。（かっことか何もなく、何もルールに違反していないため）
        return 1

    d = {"{": "}", "[": "]", "(": ")"}
    stack = []
    for i in S:
        if i in d.keys():
            stack.append(d[i])
        if i in d.values():
            if len(stack) >= 1:
                s = stack.pop()
                if i != s:
                    return 0
            else:
                return 0

    # もしstackに閉じる方のカッコがまだ残っている場合はfalse
    if len(stack) != 0:
        return 0

    return 1
