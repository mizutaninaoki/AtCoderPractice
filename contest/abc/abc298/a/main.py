n = int(input())
s = input()

ans = False
for i in s:
    if i == "o":
        ans = True
    elif i == "x":
        print("No")
        exit()
if ans:
    print("Yes")
else:
    print("No")