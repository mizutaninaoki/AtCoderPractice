# from itertools import groupby

# s = input()
# ans = []
# for k, v in groupby(s):
#     list_v = list(v)
#     ans.append((len(list_v), int(list_v[0])))
# print(*ans)

import itertools 
s = input()
for key, group in itertools.groupby(s):
        print(f"({len(list(group))}, {key})",end=' ')