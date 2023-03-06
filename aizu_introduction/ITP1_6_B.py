# 47
# S 10
# S 11
# S 12
# S 13
# H 1
# H 2
# S 6
# S 7
# S 8
# S 9
# H 6
# H 8
# H 9
# H 10
# H 11
# H 4
# H 5
# S 2
# S 3
# S 4
# S 5
# H 12
# H 13
# C 1
# C 2
# D 1
# D 2
# D 3
# D 4
# D 5
# D 6
# D 7
# C 3
# C 4
# C 5
# C 6
# C 7
# C 8
# C 9
# C 10
# C 11
# C 13
# D 9
# D 10
# D 11
# D 12
# D 13


# S 1
# H 3
# H 7
# C 12
# D 8


n = int(input())

s = []
h = []
c = []
d = []


for i in range(n):
    mark, num = input().split()
    num = int(num)

    if mark == "S":
        s.append(num)
    elif mark == "H":
        h.append(num)
    elif mark == "C":
        c.append(num)
    elif mark == "D":
        d.append(num)


for k, v in {"S": s, "H": h, "C": c, "D": d}.items():
    for j in range(1, 14):
        if not j in v:
            print(k, j)

