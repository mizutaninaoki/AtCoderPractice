s = input()
t = input()

min_cnt = 10**8
for i in range(0, len(s)-len(t)+1):
    cnt = 0
    for j in range(i, len(t) + i):
        if s[j] != t[j-i]:
            cnt += 1

    min_cnt = min(min_cnt, cnt)
print(min_cnt)
