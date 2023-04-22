n = int(input())
s = input()

prev = None
bar_idx = -1
cnt = 0
ans = -1
for idx, i in enumerate(s):
    if idx == n - 1 and i == "o":
        if bar_idx != -1:
            ans = max(ans, idx - bar_idx)
            cnt = 0
        prev = "o"
    elif i == "o":
        cnt += 1
        prev = "o"
    elif prev == "o" and i == "-":
        ans = max(ans, cnt)
        cnt = 0
        prev = "-"
        bar_idx = idx
    elif i == "-":
        prev == "-"
        bar_idx = idx

if ans == -1:
    print(-1)
    exit()
print(max(ans, cnt))


# 30
# -o-o-oooo-oo-o-ooooooo--oooo-o