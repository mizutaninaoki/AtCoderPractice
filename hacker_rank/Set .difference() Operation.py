n1 = int(input())
b1 = set(map(int, input().split()))
n2 = int(input())
b2 = set(map(int, input().split()))

print(len(b1.difference(b2)))
