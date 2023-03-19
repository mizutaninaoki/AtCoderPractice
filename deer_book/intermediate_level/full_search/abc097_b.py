x = int(input())

ans = 0
for i in range(1, 1001):
    for j in range(2, 1001):
        if not i**j <= x:
            break
        ans = max(ans, i**j)
print(ans)
