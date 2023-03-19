from itertools import combinations
n = int(input())
l = list(map(int, input().split()))
l.sort()

ans = 0
for a, b, c in combinations(l, 3):
    # ３辺の長さは全て異なる条件があるため、[4, 4, 5]みたいな組み合わせを排除するために、len(set([a, b, c])) == 3を入れている
    # また、combinationsを使っているため、[4, 5, 7]と[7, 5, 4]みたいな順番だけ違う重複は排除されている。(重複を許す場合は、combinations_with_replacementを使う)
    if len(set([a, b, c])) == 3 and a + b > c:
        ans += 1
print(ans)


# 三角形の成立条件
# 三角形は2つの辺の長さの和は残りの1つの辺の長さより大きいという特徴があります。 つまり、三角形の3辺の長さを a，b，c とするとき、次の三つの不等式が成り立ちます。
# a < b+c
# b < a+c
# c < a+b


# -------------------------
# ループで回して解く方法
# -------------------------
n = int(input())
l = list(map(int, input().split()))
l.sort()

ans = 0
for i in range(n-2):
 for j in range(i+1, n-1):
  for k in range(j+1, n):
   if l[i]+l[j] > l[k] and l[i] != l[j] and l[j] != l[k]:
    ans += 1

print(ans)
