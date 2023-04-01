# n = int(input())
# s = input()

# from collections import Counter
# counter = Counter(s)
# if len(s) == 1:
#     print("Yes")
#     exit()
# print("Yes") if counter["F"] == counter["M"] else print("No")



n = int(input())
s = input()

if len(s) == 1:
    print("Yes")
    exit()

odd_num = True
if s[0] == "M":
    for i in s:
        if odd_num and i != "M":
            print("No")
            exit()
        elif not odd_num and i != "F":
            print("No")
            exit()
        odd_num = not odd_num
            
        
if s[0] == "F":
    for j in s:
        if odd_num and j != "F":
            print("No")
            exit()
        elif not odd_num and j != "M":
            print("No")
            exit()
        odd_num = not odd_num
print("Yes")