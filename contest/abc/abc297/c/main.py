h, w = map(int, input().split())


for i in range(h):
    s = list(input())
    
    for j in range(len(s)-1):
        # if j >= 2 and (s[j] == "T" and s[j-1] == "C" and s[j-2] == "P"):
        #     continue
            
        if s[j] == "T" and s[j+1] == "T":
            s[j] = "P"
            s[j+1] = "C"
            
    
    print("".join(s))
    