n = int(input())
L = list(map(int, input().split()))
L.sort(reverse=True)

cnt = 10000000000
for i in range(n // L[0] + 1):
    a = n - i * L[0]
    for j in range(a // L[1] + 1):
        b = a - j * L[1]
        if b % L[2] == 0:
            cnt = min(cnt, i + j + b // L[2])
print(cnt)
