s = input()

b_idxs = []
r_idxs = []
k_idx = None
for idx, i in enumerate(s):
    if i =="B":
        b_idxs.append(idx)
    elif i == "R":
        r_idxs.append(idx)
    elif i == "K":
        k_idx = idx

if b_idxs[0] % 2 == 0 and b_idxs[1] % 2 == 0 or b_idxs[0] % 2 == 1 and b_idxs[1] % 2 == 1:
    print("No")
    exit()
    
if min(r_idxs) < k_idx < max(r_idxs):
    print("Yes")
else:
    print("No")