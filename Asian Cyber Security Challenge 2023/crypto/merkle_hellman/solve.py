b = [7352, 2356, 7579, 19235, 1944, 14029, 1084]
c = [8436, 22465, 30044, 22465, 51635, 10380, 11879, 50551, 35250, 51223, 14931, 25048, 7352, 50551, 37606, 39550]

flag = ""
for c_ in c:
    for kumiawase in range(pow(2, len(b))):
        s = 0
        for i in range(7):
            if kumiawase & (64 >> i):
                s += b[i]
        if s == c_:
            flag += chr(kumiawase)

print(flag)
# ACSC{E4zY_P3@zy}
