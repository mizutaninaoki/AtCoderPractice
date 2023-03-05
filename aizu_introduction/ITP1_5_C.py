# 3 4
# 5 6
# 3 3
# 2 2
# 1 1
# 0 0

# #.#.
# .#.#
# #.#.

# #.#.#.
# .#.#.#
# #.#.#.
# .#.#.#
# #.#.#.

# #.#
# .#.
# #.#

# #.
# .#

# #

while True:
    h, w = map(int, input().split())

    if (h, w) == (0, 0):
        break

    for i in range(0, h):
        line = ""
        # 奇数列の時(0 % 2 -> 0)
        if i % 2 == 1:
            for j in range(w):
                if j % 2 == 0:
                    line += "#"
                else:
                    line += "."
        # 偶数列の時(1 % 2 -> 1) 余りが1の時、偶数列になる。ややこしい。。。
        else:
            for j in range(w):
                if j % 2 == 0:
                    line += "."
                else:
                    line += "#"
        print(line)

    print()

