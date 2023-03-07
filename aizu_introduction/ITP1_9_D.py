# abcde
# 3
# replace 1 3 xyz
# reverse 0 2
# print 1 4

# xaze


s = input()
n = int(input())

for i in range(n):
    q = list(input().split())
    q[1], q[2] = int(q[1]), int(q[2])

    if q[0] == "replace":
        s = s[:q[1]] + q[3] + s[q[2]+1:]
    elif q[0] == "reverse":
        s = s[:q[1]] + "".join(reversed(s[q[1]:q[2]+1])) + s[q[2]+1:]
        # 下記の方がすっきり描けるかも（[::-1]を使うやり方）
        # s = s[:q[1]] + (s[q[1]:q[2]+1])[::-1] + s[q[2]+1:]
    else:
        print(s[q[1]:q[2]+1] )