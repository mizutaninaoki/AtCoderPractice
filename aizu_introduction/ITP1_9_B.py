# aabc
# 3
# 1
# 2
# 1
# vwxyz
# 2
# 3
# 4
# -

# aabc
# xyzvw


while True:
    s = input()
    if s == "-": break

    m = int(input())
    for i in range(m):
        h = int(input())
        tmp = s[:h]
        s = s[h:] + tmp
    print(s)
