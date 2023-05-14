if __name__ == '__main__':
    N = int(input())

    ans = []
    for i in range(N):
        cmd, *pos = input().split()
        if pos:
            pos = list(map(int, pos))

        if cmd == "insert":
            ans.insert(pos[0], pos[1])
        elif cmd == "remove":
            if pos[0] in ans:
                ans.remove(pos[0])
        elif cmd == "append":
            ans.append(pos[0])
        elif cmd == "sort":
            ans.sort()
        elif cmd == "reverse":
            ans.reverse()
        elif cmd == "pop":
            if ans:
                ans.pop()
        elif cmd == "print":
            print(ans)
