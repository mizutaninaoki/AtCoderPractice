# dream dreamer erase eraser


# dreameraser

# YES

#
# 自分の解けなかった解法
#

# s = input()
# t = ""

# count = 0

# no = 0

# d = {"dream": 5, "dreamer": 7, "erase": 5, "eraser": 6}

# while True:
#     for k, v in d.items():
#         count += v

#         if s[-v:] == k:
#             t += k
#         else:
#             count -= v

#         if s == t:
#             print("YES")
#             exit()
        
#         if no > 8:
#             print("NO")
#             exit()


#
# お手本の解法
#

s = input()
t = ""

idx = 0
fi = ['dream', 'erase']
si = 'eraser'
se = 'dreamer'

while idx < len(s):

    if s[idx:idx+6]==si and (idx+9<len(s) and s[idx+6:idx+9] != 'ase' or idx+6==len(s)):
        idx += 6
    elif s[idx:idx+7]==se and (idx+10<len(s) and s[idx+7:idx+10] != 'ase' or idx+7==len(s)):
        idx += 7
    elif s[idx:idx+5] in fi:
        idx += 5
    else:
        print("NO")
        exit()

    if idx == len(s):
        print("YES")
        exit()

print("NO")