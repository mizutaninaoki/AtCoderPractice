a, b = map(int, input().split())
s = input()

if len(s) == a+b+1 and "-" not in s[:a]+s[-b:] and s[a] == "-":
    print("Yes")
else:
    print("No")
