# -----------------------------
# 自分の答え（TLE）
# -----------------------------
# import collections
# import itertools
# k, s = map(int, input().split())
# deque = collections.deque()

# L = [i for i in range(k+1)]
# comb = itertools.combinations_with_replacement(L, 3)

# cnt = 0
# for o in comb:
#     if sum(o) == s:
#         deque.append(o)

# for idx, i in enumerate(deque):
#     l = set(list(itertools.permutations(i)))
#     for j in l:
#         if sum(j) == s:
#             cnt += 1
# print(cnt)


# まず、変数 X, Y, Z の組を全探索して、X + Y + Z = S となる組を数え上げることを考えます。各変数を 0 から K まで回す 3 重ループだと、時間計算量は O(K3) となります。
# ただし、K の上限は 2500 であるため、このままでは間に合いません。
# そこで、X + Y + Z = S に注目します。変数 X と Y が決まると、変数 Z の値は S − X − Y に決まります。
# これを利用すると、変数 X, Y の組を全探索して、変数 Z の値が 0 以上かつ K 以下であるような組を数えると、答えが求まります。この解法の時間計算量は、O(K2) となるため間に合います。
# -----------------------------
# 他者の答え（TLE）
# -----------------------------
k, s = map(int, input().split())
ans = 0

for x in range(0, k+1):
    for y in range(0, k+1):
        # s-(x+y)はつまりzの値。このzの値はsから(x+y)を引いた値のため、X + Y + Z = Sの条件はクリアしている。
        # さらにz、つまり「s-(x+y)」が0以上k以下であればzとなりうる条件もクリアするので、プラス１カウントするようにする。
        if 0 <= s-(x+y) <= k:
            ans += 1

print(ans)
