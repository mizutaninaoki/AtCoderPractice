n = int(input())
s = input()

flag1 = False
flag2 = False
flag3 = False
idx = float("inf")
for i in range(n):
    if flag1 == True and flag2 == False and s[i] == "*":
        flag2 = True
        idx = i
    elif flag1 == True and s[i] == "|" and flag3 == False and idx < i:
        print("in")
        exit()
    elif flag1 == False and s[i] == "|":
        flag1 = True
        idx = float("inf")
    elif flag1 == True and s[i] == "|":
        idx = float("inf")
        
print("out")
        
        
    