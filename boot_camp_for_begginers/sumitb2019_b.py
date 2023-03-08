# 432

# 400


# import math

# x = int(input())

# # x_without_tax = int(math.floor(x / 1.08))
# x_floor_tax = int(math.floor(x / 1.08))
# x_ceil_tax = int(math.ceil(x / 1.08))

# # x_after = int(math.floor(x_without_tax * 1.08))
# x_after_floor = int(math.floor(x_floor_tax * 1.08))
# x_after_ceil = int(math.floor(x_ceil_tax * 1.08))

# if x == x_after_floor:
#     print(x_floor_tax)
# elif x == x_after_ceil:
#     print(x_ceil_tax)
# else:
#     print(":(")


#---------------------------------------------
# 上のやり方でもできるが、全探索した方が簡単
#---------------------------------------------
import math

x = int(input())

found = False
for n in range(1, 50001):
    x_in_tax = int(math.floor(n * 1.08))
    if x_in_tax == x:
        print(n)
        found = True
        break

if not found:
    print(":(")
