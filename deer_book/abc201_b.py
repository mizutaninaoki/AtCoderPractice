n = int(input())
l = []

for i in range(n):
    s, t = input().split()
    t = int(t)
    l.append([t, s])
# 二重配列の場合、二重配列の中の最初のインデックスの値を基準にソートする
print(sorted(l, reverse=True)[1][1])

# 二重配列で、ソートするインデックスを指定する場合、keyを使う！！！
# sorted(l, reverse=True, key=lambda x: x[1])
