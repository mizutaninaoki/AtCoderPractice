inp = input()
for i in ["+", "-"]:
    a = int(inp[0]) + int(inp[1]) if i == "+" else int(inp[0]) - int(inp[1])
    for j in ["+", "-"]:
        b = a + int(inp[2]) if j == "+" else a - int(inp[2])
        for k in ["+", "-"]:
            c = b + int(inp[3]) if k == "+" else b - int(inp[3])
            if c == 7:
                print(inp[0], i, inp[1], j, inp[2], k, inp[3], "=7", sep="")
                exit()
