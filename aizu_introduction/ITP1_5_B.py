# 3 4
# 5 6
# 3 3
# 0 0

####
#..#
####

######
#....#
#....#
#....#
######

###
#.#
###


while True:
    h, w = map(int, input().split())

    if (h, w) == (0, 0):
        break

    for i in range(0, h):
        if i == 0 or i == h-1:
            print("#"*w)
        else:
            period = w - 2
            print("#" + "."*period + "#")

    print("")