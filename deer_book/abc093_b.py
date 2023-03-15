a, b, k = map(int, input().split())

cnt = 0
l = []
while cnt < k:
    l.append(a)
    if a >= b:
        break
    cnt += 1
    a += 1


cnt = 0
while cnt < k:
    l.append(b)
    if b <= a:
        break
    cnt += 1
    b -= 1

# 重複排除はset()を使う！！！
for i in sorted(list(set(l))):
    print(i)
