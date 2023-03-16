n = int(input())
t, a = map(int, input().split())
l = list(map(int, input().split()))

diff = 1000000000
result = 0
for i, h in enumerate(l, 1):
    tmp = abs(a - (t - h * 0.006))
    if tmp < diff:
        diff = tmp
        result = i
print(result)
