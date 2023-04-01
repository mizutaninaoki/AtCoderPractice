# n, x = map(int, input().split())
# l = list(map(int, input().split()))

# for i in l:
#     for j in l:
#         if i - j == x:
#             print("Yes")
#             exit()
# print("No")



# n, x = map(int, input().split())
# l = list(map(int, input().split()))

# for idx, i in enumerate(l):
#     for j in l[idx:]:
#         if i - j == x or j - i == x:
#             print("Yes")
#             exit()
# print("No")


n, x = map(int, input().split())
l = list(map(int, input().split()))

from collections import deque

que = deque()
for idx, i in enumerate(l):
    m = x + i
    que.append(m)

a = set(que) & set(l)
print("Yes") if a else print("No")