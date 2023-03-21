# L = [list(map(int, input().split())) for _ in range(3)]

# # for i in range(101):
# #     a1, a2, a3, b1, b2, b3 = 1,1,1,1,1,1

# a1, a2, a3, b1, b2, b3 = 0, 0, 0, 0, 0, 0
# al = [a1, a2, a3]
# bl = [b1, b2, b3]
# for idx_a, a in enumerate(al):
#     for idx_b, b in enumerate(bl):
#         if a + b != L[idx_a][idx_b]:
#             print("No")
#             exit()
# print("Yes")


# ---------------------------
# 　他者の解答その１
# ---------------------------
# C - Takahashi's Information
c = [input().split() for i in range(3)]
a = []
b = []
for i in range(3):
    b.append(int(c[0][i]) - 0)
for i in range(3):
    a.append(int(c[i][0]) - b[0])
for i in range(3):
    for j in range(3):
        if a[i] + b[j] != int(c[i][j]):
            exit(print("No"))

print("Yes")


# ---------------------------
# 　他者の解答その２
# ---------------------------
c = [list(map(int, input().split())) for _ in range(3)]
for i in range(101):
    for j in range(101):
        for k in range(101):
            b1 = c[0][0] - i
            b2 = c[0][1] - i
            b3 = c[0][2] - i

            if j == c[1][0] - b1 and j == c[1][1] - b2 and j == c[1][2] - b3 and k == c[2][0] - b1 and k == c[2][1] - b2 and k == c[2][2] - b3:
                print("Yes")
                exit()

print("No")
