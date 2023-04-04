# flagで判別しなくてもいけるやり方
def solution(N):
    N = bin(N)[2:]
    b = 0
    maxb = 0
    for k in N:
        if int(k) == 0:
            b += 1
        elif int(k) == 1:
            maxb = max(b, maxb)
            b = 0
    return maxb


# def solution(N: int) -> int:
#     n_bit_flags = [1 if N & 2**i else 0 for i in range(31)]

#     max_count = 0
#     counting = False
#     count = 0

#     for bit in n_bit_flags:
#         if bit:
#             counting = True
#             if count > 0:
#                 if max_count < count:
#                     max_count = count
#                 count = 0
#         else:
#             if counting:
#                 count += 1

#     return max_count
