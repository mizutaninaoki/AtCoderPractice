s, t = map(int, input().split())

cnt = 0
for i in range(101):
    for j in range(101):
        if i + j > 100 or i * j > 10000:
            break
        for k in range(101):
            if i + j + k <= s and i * j * k <= t:
                cnt += 1

            if i + j + k > 100 or i * j * k > 10000:
                break
print(cnt)


# -----------------------------
# 他者の解答
# -----------------------------
s, t = map(int, input().split())
cnt = 0
for a in range(s+1):
    # s+1-aみたいに、だんだん減らしてループさせるやり方できるようにする！
    for b in range(s+1-a):
        for c in range(s+1-a-b):
            if a+b+c <= s and a*b*c <= t:
                cnt += 1
print(cnt)
