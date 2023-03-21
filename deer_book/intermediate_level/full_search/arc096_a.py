# a, b, c, x, y = map(int, input().split())

# ans = 0
# for i in range(10001):
#     for j in range(10001):
#         for k in range(10001):
#             if (i == x and j == y) or (i * (k * 0.5) == x and j * (k * 0.5) == y):
#                 ans = min(ans, i * x + j * y + k * c)
# print(ans)


# a, b, c, x, y = map(int, input().split())
# ans = 1000000000
# t = a * x + b * y
# for i in range(x+1):
#     for j in range((t - a * x) / b):
#         k = x + y - (i + j)
#         if k < 0:
#             break
#         if (i == x and j == y) or (i + (k * 0.5) == x and j + (k * 0.5) == y):
#             ans = min(ans, i * a + j * b + k * c)
# print(ans)

# -----------------------------
# 他者の解答
# -----------------------------
A, B, C, X, Y = map(int, input().split())
mx = max(X, Y)
mn = min(X, Y)
ans = A * X + B * Y
for i in range(mx+1):
  # i枚ずつ減らす代わりに、Cを１枚ずつ増やして、最小値を求める
  ans = min(ans, A*max(X-i, 0)+B*max(Y-i, 0)+C*2*i)
print(ans)
