# 1
# 10
# 2

# 4


n = int(input())
k = int(input())
l = list(map(int, input().split()))

ans = 0
for i in l:
    ans += 2 * min(abs(i), abs(k-i))

print(ans)
