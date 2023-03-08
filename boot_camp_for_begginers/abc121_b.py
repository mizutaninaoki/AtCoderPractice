# 2 3 -10
# 1 2 3
# 3 2 1
# 1 2 2


# 1


n, m ,c = map(int, input().split())
b_list = list(map(int, input().split()))

ans = 0
for i in range(n):
    a_list = list(map(int, input().split()))

    total = 0
    for a, b in zip(a_list, b_list):
        total += a*b
    total += c

    if total > 0:
        ans += 1

print(ans)




