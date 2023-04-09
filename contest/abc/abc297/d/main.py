a, b = map(int, input().split())

cnt = 0


if a == b:
    print(cnt)
    exit()

while a != b:
    if a > b:
        mod = a % b
        cnt += a // b
        if mod == 0:
            break
        a = mod
    elif a < b:
        mod = b % a
        cnt += b // a
        if mod == 0:
            break
        b = mod

print(cnt-1)




# while a != b:
#     if a > b:
#         mod = a % b
#         if a // b == 1:
#             cnt += a // b - 1
#         else:
#             cnt += a // b
#         if mod == 0:
#             break
#         a = mod
#     elif a < b:
#         mod = b % a
#         if b // a == 1:
#             cnt += b // a - 1
#         else:
#             cnt += b // a
#         if mod == 0:
#             break
#         b = mod
#     print(cnt)
#     print(a, b)
#     print("------------")

# print(cnt)


# while a != b:
#     if a % 2 == 0 and b % 2 == 0:
#         pass
#     else:
#         if a > b:
#             mod = a % b
#             if mod == 1:
#                 cnt += b
#                 break
#             else:
#                 cnt += a // b
#                 b = mod
#         elif a < b:
#             mod = b % a
#             if mod == 1:
#                 cnt += a
#                 break
#             else:
#                 cnt += b // a
#                 a = mod
