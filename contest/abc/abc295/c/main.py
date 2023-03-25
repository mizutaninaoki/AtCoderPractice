import collections
n = int(input())
L = list(input().split())

ans = 0
for v in collections.Counter(L).values():
    ans += int(v) // 2
print(ans)
