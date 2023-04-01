# n, m = map(int, input().split())

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         seki = i * j
#         if seki >= m:
#             print(seki)
#             exit()
# print(-1)

# import math
# n, m = map(int, input().split())
# if n**2 >= m:
#     num = math.sqrt(m) // 1
#     num2 = 0
#     if m % 2 == 0:
#         num2 = m // 2
#     else: num2 = m // 2 + 1
#     print(int(num * num2))
# else:
#     print(-1)


# -------------------------
# 自分の解答(WA)
# -------------------------
# import math
# n, m = map(int, input().split())
# if n**2 >= m:
#     num = int(math.sqrt(m))
#     for i in range(2, n+1):
#         if m % i == 0:
#             print(m*i)
#             exit()
#         if m % (i + 1) == 0:
#             print(m*i)
#             exit()

# else:
#     print(-1)


# -------------------------
# 他者の解答
# -------------------------
n, m = map(int, input().split())
if n*n < m:
    exit(print(-1))

ans = n*n
# mのルートまで見て、全探索して、minを取る。
for i in range(1, int(m**0.5)+1):
    if i*n >= m:
        # i*(((m-1)//i)+1) の部分はよくわからないが、こういうことをすれば解答に辿り着く法則性があるのだと思う。。。
        ans = min(ans, i*(((m-1)//i)+1))
print(ans)
