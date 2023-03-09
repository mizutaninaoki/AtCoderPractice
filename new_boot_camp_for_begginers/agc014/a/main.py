# 4 12 20

# 3


a, b, c = map(int, input().split())

cnt = 0
while a % 2 == 0 and b % 2 == 0 and c % 2 == 0:

    if a == b == c:
        print(-1)
        exit()

    a_tmp = b // 2 + c // 2
    b_tmp = c // 2 + a // 2
    c_tmp = a // 2 + b // 2

    a = b_tmp + c_tmp
    b = c_tmp + a_tmp
    c = a_tmp + b_tmp

    cnt += 1

print(cnt)
