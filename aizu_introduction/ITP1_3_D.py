# 5 14 80

# 3


a, b ,c = map(int, input().split())
cnt = 0

for i in range(a, b+1):
    if c % i == 0:
        cnt += 1

print(cnt)