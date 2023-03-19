h, w, x, y = map(int, input().split())
l = [input() for _ in range(h)]
cnt = 0

# 左側
for i in l[x-1][:y-1][::-1]:
    if i == ".":
        cnt += 1
    else:
        break

# 右側（自分の点も含む）
for j in l[x-1][y-1:]:
    if j == ".":
        cnt += 1
        continue
    break

# 上側
for k in l[:x-1][::-1]:
    if k[y-1] == ".":
        cnt += 1
        continue
    break

# 下側
for m in l[x:]:
    if m[y-1] == ".":
        cnt += 1
        continue
    break

print(cnt)
