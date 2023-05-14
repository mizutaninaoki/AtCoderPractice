import textwrap


def wrap(string, max_width):
    # length = len(string)
    # ans = ""
    # start = 0
    # for i in range(length+1):
    #     ans += string[start:start+max_width] + "\n"
    #     start += max_width
    # return ans

    # このコードが一番簡潔
    return textwrap.fill(string, max_width)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
