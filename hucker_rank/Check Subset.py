T = int(input())

for _ in range(T):
    n1 = int(input())
    A = set(map(int, input().split()))
    n2 = int(input())
    B = set(map(int, input().split()))

    print(True) if A <= B else print(False)
