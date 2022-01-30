with open("flag.txt") as f:
    enc_flag = f.read()

flag = [""]*len(enc_flag)
idx = 0

for i in range(len(enc_flag)):
    flag[idx] = enc_flag[i]
    if i % 1000000 == 0:
        print(i)
    idx += 1
    if idx > 7 and "".join(flag[idx-8:idx]).lower() == "<script>":
        idx -= 8

flag = "".join(flag)
print(flag[:flag.index("}")+1])
