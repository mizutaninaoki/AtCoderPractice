n = int(input())
l = list(map(int, input().split()))

ans = []
for i in l:
    if i % 2 == 0:
        ans.append(i)
print(*ans)