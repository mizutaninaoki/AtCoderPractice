def solution(H: [int]) -> int:
    stack = []
    walls = 0

    for i in H:
        if len(stack) == 0:
            stack.append(i)
            walls += 1
        else:
            if i > stack[-1]:
                stack.append(i)
                walls += 1
            elif i < stack[-1]:
                while len(stack) > 0:
                    last_wall = stack.pop()
                    if last_wall == i:
                        walls -= 1
                        break
                    elif last_wall < i:
                        stack.append(last_wall)
                        break
                stack.append(i)
                walls += 1

    return walls
