l = []
tmp_sc = set()
for _ in range(int(input())):
    name = input()
    score = float(input())

    l.append([name, score])
    tmp_sc.add(score)

tmp_sc = sorted(list(tmp_sc))
ans = []
for i in l:
    if tmp_sc[1] == i[1]:
        ans.append(i[0])
ans.sort()
for j in ans:
    print(j)
