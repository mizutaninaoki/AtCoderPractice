# n = int(input())
# l = list(map(int, input().split()))

# total = sum(l)
# if total % 10 != 0:
#     print("No")
#     exit()


# just_piece = total // 10

# if just_piece in l:
#     print("Yes")
#     exit()

# piece = 0
# start = 0
# end = 2
# while piece <= just_piece:
#     l[start:end]


# prev = l[0]
# for i in l[1:]:
#     if sum(l) // (prev + i) == 10:
#         print("Yes")
#         exit()
#     prev = i

# if sum(l) // (l[0] + l[-1]) == 10:
#     print("Yes")
#     exit()

# print("No")


# ---------------------
# 他者の解答
# ---------------------
import itertools
N = int(input())
A = list(map(int, input().split()))
A_10 = sum(A)/10
A = A+A  # Aの配列を２つくっつけている(最初と最後のピースをくっつけるパターンを検証するため)
# itertools.accumulateで累積和を持つitertools.accumulate objectを返すので、list()で配列化する
B = list(itertools.accumulate(A))
k = 0
for i in range(N+1):
    # 2*N-1はA=A+Aで２つの配列をくっつけたから
    # B[k]-B[i]で２つのピースをくっつけた場合、３つのピースをくっつけた場合...と順番に検証している
    while k < 2*N-1 and B[k]-B[i] < A_10:
        k += 1
    if B[k]-B[i] == A_10:
        print("Yes")
        exit()
print("No")
