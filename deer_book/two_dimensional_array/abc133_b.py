import math
n, d = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
# listにて、指定で:を入れる場合、はみ出してもout of indexにはならず空のリストが返ってくる。
for idx, i in enumerate(l):
    for j in l[idx+1:]:
        point = 0
        for i2, j2 in zip(i, j):
            point += abs(i2 - j2)**2
        if int(math.sqrt(point)) == math.sqrt(point):
            cnt += 1
print(cnt)

# # ------------------------------------------
# # リストの範囲指定に関するTips(listにて、指定で:を入れる場合、はみ出してもout of indexにはならず空のリストが返ってくる。)
# # ------------------------------------------
# a = ["a", "b", "c"]

# # インデックスで4だけ指定すると、エラーになる。
# print(a[4])
# # IndexError: list index out of range

# # 最後より先のインデックスを範囲指定すると、空の配列が返ってくる
# print(a[4:])
# # []

# # 最後より先のインデックスより前を範囲指定すると、値が存在する、つまり全ての配列が返ってくる。
# print(a[:4])
# # ['a', 'b', 'c']
