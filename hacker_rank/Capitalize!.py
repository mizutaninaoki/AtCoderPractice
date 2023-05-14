# Complete the solve function below.
def solve(s):
    # ans = ""
    # prev = ""
    # for st in s:
    #     if prev == "" or prev == " ":
    #         ans += st.upper()
    #     else:
    #         ans += st
    #     prev = st

    # return ans

    # スペースごとにsplit()で分割して、単語の先頭の文字を大文字に変換してから、" ".join()で空白区切りでつなげている
    return ' '.join([i.capitalize() for i in s.split(' ')])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
