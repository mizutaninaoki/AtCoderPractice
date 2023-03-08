# 4 5

# 10

h, w = map(int, input().split())

board = h*w

# w == 0の条件は必要ないらしい。。。
# if w == 0:
#     print(0)
#     exit()

if h == 1:
    print(1)
elif w == 1:
    print(1)
elif board % 2 == 0:
    print(board // 2)
else:
    print((board // 2) + 1)