# 3
# cat dog
# fish fish
# lion tiger

# 1 7


n = int(input())

taro = 0
hanako = 0
for i in range(n):
    taro_str, hanako_str = input().split()

    if taro_str > hanako_str:
        taro += 3
    elif taro_str < hanako_str:
        hanako += 3
    else:
        taro += 1
        hanako += 1

print(taro, hanako)
