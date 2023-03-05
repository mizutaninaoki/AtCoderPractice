# 1 + 2
# 56 - 18
# 13 * 2
# 100 / 10
# 27 + 81
# 0 ? 0

# 3
# 38
# 26
# 10
# 108

while True:
    a, op, b = input().split()
    a, b = int(a), int(b)

    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        # 割り切れない時は小数点以下を切り捨てる条件があるため、//を使う
        print(a // b)
    else:
        break

