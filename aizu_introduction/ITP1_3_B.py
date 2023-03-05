# 3
# 5
# 11
# 7
# 8
# 19
# 0

# Case 1: 3
# Case 2: 5
# Case 3: 11
# Case 4: 7
# Case 5: 8
# Case 6: 19

for i in range(1, 10001):
    n = int(input())

    if n == 0:
        break
    else:
        print(f"Case {i}: {n}")
