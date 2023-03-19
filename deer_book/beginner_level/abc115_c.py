n, k = map(int, input().split())
l = sorted([int(input()) for _ in range(n)])

result = 1000000000
for i, v in enumerate(l):
    result = min(result, l[i+k-1] - l[i])
    if i+k == n:
        break
print(result)
