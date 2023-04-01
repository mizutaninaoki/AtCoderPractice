s = [input() for _ in range(8)]

num_l = [8,7,6,5,4,3,2,1]
str_l = ["a", "b", "c", "d", "e", "f", "g", "h"] 

for idx1, i in enumerate(s):
    for idx2, j in enumerate(i):
        if j == "*":
            print(str_l[idx2] + str(num_l[idx1]))
            exit()