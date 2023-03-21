# a, b, w = map(int, input().split())

# min_ans = 1000
# max_ans = 0
# flag = False
# for i in range(1001):
#     for j in range(1001):
#         if a * i + b * j == w * 1000:
#             min_ans = min(min_ans, i + b)
#             max_ans = max(max_ans, i + b)
#             flag = True
# if flag:
#     print(min_ans, max_ans)
# else:
#     print("UNSATISFIABLE")


# ----------------------------
# 他者の答え（その１）
# ----------------------------
a, b, w = map(int, input().split())
ans = []
for i in range(1, 1 + 10**6):
    if w * 1000 / i >= a and w * 1000 / i <= b:
        ans.append(i)

if len(ans) != 0:
    print(min(ans), max(ans))
else:
    print("UNSATISFIABLE")


# ----------------------------
# 他者の答え（その２）
# ----------------------------
A, B, W = map(int, input().split())
MI = W*1000//B
MA = W*1000//A
if MI > MA:
    print('UNSATISFIABLE')
else:
    print(MI, MA)
