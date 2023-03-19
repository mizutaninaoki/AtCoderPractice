n, x = map(int, input().split())
l = list(map(int, input().split()))

cnt = 0
d = 0
# 配列lの先頭に0を追加
l.insert(0, 0)
for i in l:
    d += i
    if x < d:
        break

    cnt += 1


print(cnt)
