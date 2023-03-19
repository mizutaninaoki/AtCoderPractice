s = input()
t = input()

if s == t:
    print("Yes")
    exit()

for i in range(0, len(s)-1):
    # 一度リストにしてから文字の置換を行わないと、string型の場合はエラーになる
    # 参考: https://qiita.com/tamago324/items/ea39fb541ef9f2cada7f
    list_s = list(s)
    list_s[i:i+2] = list_s[i+1] + list_s[i]
    if "".join(list_s) == t:
        print("Yes")
        exit()

print("No")
