def cold(t):
    return t[17:] + t[0:17]

def cold_rev(t):
    return t[16:] + t[0:16]

def cool_rev(t):
    s = ""
    for i in range(len(t)):
        if i % 2 == 0:
            s += chr(ord(t[i]) - 3 * (i//2))
        else:
            s += t[i]
    return s


def warm_rev(t, i):
    a = t[0: t.find("l") + 1]
    t1 = t[t.find("l") + 1:]
    return t1 + a[i:] + a[:i]


def hot_rev(t):
    adj = [-72, 7, -58, 2, -33, 1, -102, 65, 13, -64, 21, 14, -45, -11, -48, -
           7, -1, 3, 47, -65, 3, -18, -73, 40, -27, -73, -13, 0, 0, -68, 10, 45, 13]
    s = ""
    for i in range(len(t)):
        s += chr(ord(t[i]) - adj[i])
    return s


match = "4n_3nd0th3rm1c_rxn_4b50rb5_3n3rgy"

print(match == cold_rev(cold(match)))

for i in range(33):
    s1 = hot_rev(match)
    s2 = warm_rev(s1, i)
    s3 = cool_rev(s2)
    s4 = cold_rev(s3)
    if "flag" in s4:
        print(s4)
