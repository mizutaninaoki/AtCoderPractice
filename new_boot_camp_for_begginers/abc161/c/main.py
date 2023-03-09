# # 7 4

# # 1

# 解答の参考：https://drken1215.hatenablog.com/entry/2020/04/05/155200
# ※ サンプル３つ目の出力が0なのは、青木君は操作を 0 回以上「好きな回数」行った時というのが条件のため、サンプル３つ目は1回も操作を行わなかった（つまり0回）

# n, k = map(int, input().split())
# print(min(n % k, k - n % k))


# -------------------------------------------
# 以下は自分で考えた解答だが、TLEになってしまう。
# -------------------------------------------
# n, k = map(int, input().split())

# # ans = 0
# prev = 0
# two_prev = 0

# cnt = 0
# while True:
#     n = abs(n-k)

#     if k == 1:
#         break

#     if two_prev == n:
#         cnt = min(two_prev, prev)
#         break

#     if cnt == 0:
#         cnt += 1
#         prev = n
#         continue
#     # elif cnt == 1:
#     #     prev = ans
#     #     cnt += 1
#     #     continue

#     two_prev = prev
#     prev = n
#     cnt += 1


# print(cnt)
