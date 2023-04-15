# 自分の解答(TLE)
# from collections import deque
# q = int(input())
# S = 1
# for i in range(q):
#     num, *x = map(int, input().split())

#     if num == 1:
#         S.append(x[0])
#     elif num == 2:
#         S = int(str(S)[1:])
#     else:
#         n = int("".join(map(str, S))) % 998244353
#         print(n)


# 他者の回答1
from collections import deque
Mod = 998244353
Q = int(input())
S = deque()
S.append(1)
ans = 1
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        S.append(query[1])
        # 「10×ans+S」でansの数字を文字列やリストに変換しないで、一番最後にquery[1]の数字をくっつけることができる。
        # 割り算以外は計算途中にあまりをとっても、最終的なあまりと同じのため、計算処理を早めるためにここでも998244353で割っておく。
        ans = (ans*10+query[1]) % Mod
    elif query[0] == 2:
        p = S.popleft()
        # 以下のような感じでpow(底数, 乗数, 割る数)を使えば、Mod(998244353)で割った余りの数が算出できる。
        # 以下は10の8乗(100000000)を998244353で割った余りを返している
        # pow(10, 8, 998244353)
        # 100000000
        # (ans-(p*pow(10, len(S), Mod)))で一番大きい位の値だけ削除している。
        # 例えば、「54321」という数字だとしたら、pには5(一番左の数字)が入っていて、len(S)は4となるため、(p*pow(10, len(S), Mod))で50000 % 998244353 => 50000が算出でき、
        # 54321 - 50000 => 4321が算出され、最後 4321 % 998244353 => 4321がansに入ることになる。
        # (割り算以外は計算途中にあまりをとっても、最終的なあまりと同じのため、計算処理を早めるためにここでも998244353で割っておく。)
        ans = (ans-(p*pow(10, len(S), Mod))) % Mod
    else:
        print(ans)
