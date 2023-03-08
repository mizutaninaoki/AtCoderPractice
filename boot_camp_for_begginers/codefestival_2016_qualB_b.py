# 10 2 3
# abccabaabb


# Yes
# Yes
# No
# No
# Yes
# Yes
# Yes
# No
# No
# No


n, a, b = map(int, input().split())
s = input()

pass_people = 0
b_pass_people = 0
for i, v in enumerate(s):
    if pass_people >= a + b:
        print("No")
    elif v == "c":
        print("No")
    elif v == "a":
        print("Yes")
        pass_people += 1
    elif v == "b":
        if b_pass_people < b:
            print("Yes")
            b_pass_people += 1
            pass_people += 1
        else:
            print("No")
