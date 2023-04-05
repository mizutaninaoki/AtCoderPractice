
# 100%
def solution(A, B):
    cnt = 0
    stack = []
    for a, b in zip(A, B):
        if b == 1:
            stack.append(a)
        else:
            # stackにいる魚と全て比較する
            while len(stack) > 0:
                if stack[-1] > a:
                    break
                else:
                    stack.pop()

            # 一番最初にbが0だった魚、もしくは現時点でstackに入っているどの魚よりも大きかった場合、cntに追加する
            if len(stack) == 0:
                cnt += 1
    # 最後にstackに残っている魚(生き残った魚)をcntに追加
    return cnt + len(stack)
