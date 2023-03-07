# 123
# 55
# 1000
# 0

# 6
# 10
# 1


while True:
    strNum = input()

    if int(strNum) == 0: break

    num = 0
    for s in strNum:
        num += int(s)
    print(num)