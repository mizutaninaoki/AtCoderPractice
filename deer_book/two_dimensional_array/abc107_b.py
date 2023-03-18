h, w = map(int, input().split())
L = [input() for _ in range(h)]

L2 = []
for i in L:
    if not all([j == "."for j in i]):
        L2.append(i)

L2 = [list(k) for k in L2]
L2 = list(zip(*L2))

L3 = []
for m in L2:
    if not all([o == "."for o in "".join(m)]):
        L3.append(m)

L3 = list(zip(*L3))

for p in L3:
    print("".join(p))


# --------------------------------------------------------------
# ループさせる配列自身をループ内で配列自身の要素を削除(popやremove)するとおかしくなる
# --------------------------------------------------------------
# 参考：haya-programming.com/entry/2018/06/02/163415
# 以下のようなコードを書くと、ループが正しく動作しない。
# ループ内で配列自身の要素を削除(popやremove)しないようにするか、内包表記で書くと大丈夫っぽい。
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for x in lst:
    if x % 2 != 0:
        lst.remove(x)

# 以下のようなコードは、配列自身の要素を削除していたため、意図した通りに動かなかった。

# h, w = map(int, input().split())
# L = [input() for _ in range(h)]

# for idx, i in enumerate(L):
#     if all([j == "."for j in i]):
#         L.pop(idx)

# print(L)
# L = [list(k) for k in L]
# L = list(zip(*L))

# for idx2, m in enumerate(L):
#     if all([o == "."for o in "".join(m)]):
#         L.pop(idx2)

# L = list(zip(*L))

# for p in L:
#     print("".join(p))
