# from collections import Counter
# import itertools
# h, w = map(int, input().split())
# A = [input() for _ in range(h)]
# B = [input() for _ in range(h)]

# # print(A)
# # ['..#',_'...',_'.#.',_'...']

# counter_a = Counter("".join(A))
# counter_b = Counter("".join(B))

# if counter_a != counter_b:
#     print("No")
#     exit()

# cA = A
# cB = B

# for u in range(h):
#     cnt = 0
#     flag = False
#     # if u != 0:
#     tmpA = cA
#     last = tmpA.pop(0)
#     tmpA.append(last)
#     cA = tmpA
#     for i, j in zip(cA, cB):
#         if Counter(i) == Counter(j):
#             cnt += 1


#     if cnt == h:
#         cA2 = list(zip(*cA))
#         cB2 = list(zip(*cB))
#         if Counter(cA2) == Counter(cB2):
#             flag = True
#             break


# if cnt != h and not flag:
#     print("No")
#     exit()


# cA = list(zip(*cA))
# cB = list(zip(*cB))

# for u in range(w):
#     cnt = 0
#     # if u != 0:
#     tmpA = cA
#     last = tmpA.pop(0)
#     tmpA.append(last)
#     cA = tmpA
#     for i, j in zip(cA, cB):
#         if Counter(i) == Counter(j):
#             cnt += 1


#     # if list(itertools.chain.from_iterable(zip(*cA))) == "".join(B):
#     #     print("Yes")
#     #     exit()


#     if cnt == w:
#         break


# if cnt != w:
#     print("No")
#     exit()

# print("Yes")


# 他者のコード
H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]
B = [list(input()) for _ in range(H)]

# １マスずつ見ていって、そこから横向き(W)に動かせる範囲と、縦向き(H)に動かせる範囲を全て動かして試していって、
# 全てBと一致することがあればYesを返すようにしている
for hs in range(H):
    for ws in range(W):
        flag = True
        for h in range(H):
            for w in range(W):
                if A[(h+hs) % H][(w+ws) % W] != B[h][w]:
                    flag = False
        if flag:
            print("Yes")
            exit()
print("No")
