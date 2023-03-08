# 6
# 382253568 723152896 37802240 379425024 404894720 471526144

loop = 0
digit = int(input())
nums = list(map(int, input().split()))

while True:
    
    for i in range(digit):

        if not nums[i] % 2 == 0:
            print(loop)
            exit()
        else:
            nums[i] = nums[i] // 2

    loop += 1



