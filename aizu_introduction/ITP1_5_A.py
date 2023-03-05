# 3 4
# 5 6
# 2 2
# 0 0

####
####
####

######
######
######
######
######

##
##


while True:
    h, w = map(int, input().split())

    # if (h, w) == (0, 0):
    #     break
    if h == w == 0:
        break

    for _ in range(h):
        print("#"*w)
    print("")