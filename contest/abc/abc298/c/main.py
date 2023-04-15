n = int(input())
q = int(input())
from collections import defaultdict, deque
from bisect import insort_left
d = defaultdict(deque)
d2 = defaultdict(set)

for z in range(q):
    num, i, *j = map(int, input().split())
    
    if num == 1:
        # insort_left(d[j[0]], i)
        d[j[0]].append(i)
        d2[i].add(j[0])
    elif num == 2:
        print(*sorted(d[i]))
        # print(*d[i])
    else:
        # box = deque()
        # for x in d2:
        #     if i in d2[x]:
        #         # insort_left(box, x)
        #         box.append(x)
        # print(*sorted(box))
        # print(*box)
        print(*sorted(d2[i]))
            
    