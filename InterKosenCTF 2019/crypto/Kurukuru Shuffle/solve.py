import re
import copy

m = "1m__s4sk_s3np41m1r_836lly_cut3_34799u14}1osenCTF{5sKm"

L = len(m)

m = list(m)

for k in range(1,L):
    for a in range(L):
        for b in range(L):
            tmp = copy.deepcopy(m)
            if a == b: break
            i = k
            for _ in range(L):
                i = (i - k) % L
                s = (i + a) % L
                t = (i + b) % L
                tmp[s], tmp[t] = tmp[t], tmp[s]
            if re.match('Kosen',"".join(tmp)):
                print("".join(tmp))
