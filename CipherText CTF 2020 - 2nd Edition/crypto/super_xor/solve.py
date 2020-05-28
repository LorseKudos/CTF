def dec(text,key):
    flag = ''
    for i in reversed(range(len(text))):
        c, text = ord(text[0]), text[1:]

        y = ord(key[i % len(key)]) + 4*i

        for _ in range(5):
            c = c ^ y
            y -= i
        flag += chr(c)
        text = text[::-1]
    return flag[::-1]

key = "cnfdnf"

with open("encrypted") as f:
    enc_flag = f.read()

print(len(list(enc_flag)))

print(dec(enc_flag, key))
