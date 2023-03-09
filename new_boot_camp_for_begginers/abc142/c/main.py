# 3
# 2 3 1

# 3 1 2

# --------------------------
# 自分の解答(TLE)
# --------------------------
# n = int(input())
# l = list(map(int, input().split()))

# ll = []
# for i in range(1, n+1):
#     for index, j in enumerate(l):
#         if i == j:
#             ll.append(index+1)

# print(*ll)


# 参考：https://blog.hamayanhamayan.com/entry/2019/09/28/230626_1
# -------------------------
# 他の人の解答
# -------------------------
n = int(input())
l = list(map(int, input().split()))
ll = [0]*n

for i in range(n):
    ll[l[i] - 1] = i+1

print(*ll)
