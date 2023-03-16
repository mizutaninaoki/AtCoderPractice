# n, m = map(int, input().split())
# l = sorted([list(map(int, input().split()))
#            for _ in range(n)], key=lambda x: x[0])

# price = 0
# cnt = 0
# for i in l:
#     for j in range(i[1]):
#         if cnt < m:
#             cnt += 1
#             price += i[0]
# print(price)


n, m = map(int, input().split())
l = sorted([list(map(int, input().split()))
           for _ in range(n)], key=lambda x: x[0])

price = 0
m_tmp = m
# 二重配列をループで回す場合、()で囲めば、それぞれの値をループ内で取り出せる！
for (a, b) in l:
    if m_tmp >= b:
        m_tmp -= b
        price += a * b
    else:
        price += a * m_tmp
        break
print(price)
