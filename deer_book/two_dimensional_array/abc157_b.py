a = [[False for _ in range(3)] for _ in range(3)]
l = [list(map(int, input().split())) for _ in range(3)]
n = int(input())
for i in range(n):
    b = int(input())
    for idx, j in enumerate(l):
        for idx2, k in enumerate(j):
            if k == b:
                a[idx][idx2] = True

for a1 in a:
    if all(a1):
        print("Yes")
        exit()

for index in range(3):
    if a[0][index] and a[1][index] and a[2][index]:
        print("Yes")
        exit()

if (a[0][0] and a[1][1] and a[2][2]) or (a[2][0] and a[1][1] and a[0][2]):
    print("Yes")
    exit()

print("No")
