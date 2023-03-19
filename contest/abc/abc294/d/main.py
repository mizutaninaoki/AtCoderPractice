# ------------------------------------------
# 自分の解答(TLE)
# ------------------------------------------
# from collections import defaultdict
# n, q = map(int, input().split())
# d = defaultdict(int)
# max_num = 0
# L = [list(map(int, input().split())) for _ in range(q)]
# for event, *x in L:
#     if event == 1:
#         max_num += 1
#         d[max_num] = max_num
#     elif event == 2:
#         d.pop(d.get(x[0]))
#     else:
#         print(list(d)[0])


# ------------------------------------------
# 他者の解答（その１）（setを使う）ベストアンサー
# ------------------------------------------
from heapq import heapify, heappop, heappush
import sys
n, q = map(int, input().split())
people = set(range(1, n+1))
for _ in range(q):
  event = list(map(int, input().split()))
  if event[0] == 2:
     # 集合はdiscardで削除
     people.discard(event[1])
  elif event[0] == 3:
      # next(iter({}))で先頭の値を取得できる
      print(next(iter(people)))


# ------------------------------------------
# 他者の解答（その２）（heapqを使う）
# ------------------------------------------
input = sys.stdin.readline

n, q = map(int, input().split())
not_call = list(range(1, n+1))
heapify(not_call)
call = []
done = set()
heapify(call)
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        mn = heappop(not_call)
        heappush(call, mn)
    elif query[0] == 2:
        done.add(query[1])
    else:
        mn = heappop(call)
        while mn in done:
            mn = heappop(call)
        print(mn)
        heappush(call, mn)


# ------------------------------------------
# 他者の解答（その3）（heapqを使う）
# ------------------------------------------
    N, Q = map(int, input().split())
    ptr = 1
    ans = []
    appear = set()
    for i in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            heappush(ans, ptr)
            ptr += 1

        if q[0] == 2:
            appear.add(q[1])
        if q[0] == 3:
            while ans:
                if ans[0] in appear:
                    heappop(ans)
                else:
                    print(ans[0])
                    break
