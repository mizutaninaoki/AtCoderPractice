# 7

# 4

# n = int(input())

# ans = 0
# for i in range(1, n+1):
#     tmp = i
#     count = 0
#     while True:
#         if tmp % 2 == 0:
#             tmp //= 2
#             count += 1
#         else:
#             if count > ans:
#                 ans = i
#             break

# print(ans)


n = int(input())

ans = 1
count = 0
for i in range(1, n+1):
    tmp = i
    tmp_count = 0
    while tmp % 2 == 0:
        tmp //= 2
        tmp_count += 1
    else:
        if tmp_count > count:
            count = tmp_count
            ans = i

print(ans)
