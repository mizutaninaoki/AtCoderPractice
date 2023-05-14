def swap_case(s):
    tmp_s = ""
    for i in s:
        if i.isupper():
            tmp_s += i.lower()
        elif i.islower():
            tmp_s += i.upper()
        else:
            tmp_s += i
    return tmp_s


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
