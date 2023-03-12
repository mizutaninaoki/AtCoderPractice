# abcdef


# badcfe

s = list(input())
s2 = s.copy()

for i in range(0, len(s2), 2):
    s[i] = s2[i+1]
    s[i+1] = s2[i]

print("".join(s))
