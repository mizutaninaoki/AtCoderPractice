# 自分の解答（時間がなかった。。。）
# n, k = map(int, input().split())
# A = sorted([int(input) for _ in range(n)])

# num = 1
# cnt = 1

# import itertools

# while cnt < k:
#     comb = set(itertools.combinations(A, num))
#     for i in range(len(A)):
#         comb.update(A[i]*num)
#     for idx, j in enumerate(comb):
#         if idx == k:
#             print(sum(j))


# 他者の解答(heapq使っている)
import heapq
n, k = map(int, input().split())
a2 = list(map(int, input().split()))
q = [0]
prev = set()

# range(k+1)をすることで、このループが終わった時、aにはk番目の最小値が入っている。
for _ in range(k+1):
    # heappopで最小値を取り出す
    a = heapq.heappop(q)
    # heapの中に最小値が重複している場合があるため、その場合は最小値が１つになるまで、whileの中でheappopで削除を繰り返すようにする。
    while a in prev:
        a = heapq.heappop(q)

    # 最小値をprevに追加
    prev.add(a)
    # 最小値をそれぞれの値に足したものをheapqに全て追加していく
    for i in a2:
        heapq.heappush(q, i+a)
print(a)
