s = input()
t = input()

if "".join(sorted(s)) < "".join(sorted(t, reverse=True)):
    print("Yes")
    exit()

print("No")
