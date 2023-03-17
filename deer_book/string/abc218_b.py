l = list(map(int, input().split()))

s = ""
for i in l:
    s += chr(i+96)
print(s)
