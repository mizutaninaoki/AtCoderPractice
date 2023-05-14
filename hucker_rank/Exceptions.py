# Enter your code here. Read input from STDIN. Print output to STDOUT

# n = int(input())

# for i in range(n):
#     first, second = input().split()
#     first = int(first)
#     if second.isdigit():
#         second = int(second)

#     try:
#         print(first // second)
#     except Exception as e:
#         print("Error Code:", e)
        
        
T = int(input())

for i in range(T):
    try:
        a, b = map(int,input().split())
        print(a//b)
    except (ZeroDivisionError, ValueError) as e:
        print('Error Code:', e)