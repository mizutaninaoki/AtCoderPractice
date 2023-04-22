# 自分の解答(WA)
# n = int(input())
# first_n = n
# cnt = 0
# prev = -1
# s = 0

# while cnt < 21:
#     cnt += 1

#     if s != prev and 1 < prev < first_n - 1:
#         print("!", s, flush=True)
#         exit()

#     n -= 1
#     print("?", n - 1, flush=True)

#     s = int(input())
#     prev = s


# 他者の解答(二分探索法)　よくわからない。。。
N = int(input())
mi = 1
ma = N
while ma - mi > 1:
    mid = (mi + ma) // 2
    print("?", mid)
    ans = int(input())
    if ans == 0:
        mi = mid
    else:
        ma = mid
print("!", mi)
