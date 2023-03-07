# 40 42 -1
# 20 30 -1
# 0 2 -1
# -1 -1 -1

# A
# C
# F

while True:
    m, f, r = map(int, input().split())

    if m == f == r == -1:
        break

    if m == -1 or f == -1:
        print("F")
        continue

    if m + f >= 80:
        print("A")
    elif m + f >= 65:
        print("B")
    elif m + f >= 50:
        print("C")
    elif m + f >= 30:
        if r >= 50:
            print("C")
        else:
            print("D")
    else:
        print("F")
