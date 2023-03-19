s = input()

for i in range(1, len(s)):
    st = s[:-i]
    st_len = len(st)

    if st_len % 2 != 0:
        continue

    if st[:(st_len // 2)] == st[(st_len // 2):]:
        print(st_len)
        break
