# 7
# 50
# 30
# 50
# 100
# 50
# 80
# 30

# 4

# #
# # 自分の答え
# #
# n = int(input())
# l = []

# for i in range(n):
#     l.append(int(input()))

# uniqueLength = len(list(set(l)))
# print(uniqueLength)



#
# 解法
#
from collections import Counter
n = int(input())
d = Counter([int(input()) for _ in range(n)])
print(len(d))

# Counterを使うと、出現回数が多い順に辞書のCounterクラスで帰ってくる。以下のような感じである。
# d = Counter([1,3, 7, 5, 7])
# Counter({7: 2, 1: 1, 3: 1, 5: 1})
# len(d) -> 4