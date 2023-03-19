from bisect import bisect_left
n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = sorted(A+B)

Al = []
for i in A:
    Al.append(bisect_left(C, i)+1)
print(*Al)

Bl = []
for j in B:
    Bl.append(bisect_left(C, j)+1)
print(*Bl)