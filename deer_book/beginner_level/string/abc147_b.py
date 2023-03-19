s = input()

half = len(s) // 2
cnt = 0
for idx, v in enumerate(s):
    if s[idx] != s[-(idx+1)]:
        cnt += 1
    if idx+1 == half:
        break

print(cnt)
