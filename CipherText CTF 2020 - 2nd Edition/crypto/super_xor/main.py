def enc(text,key):
    enc_flag = ''
    i = 0
    while i < len(text):
        x = ord(text[i])
        y = ord(key[i % len(key)])
        res = (x ^ y)
        y += i
        res = (res | y)-(res & y)
        y += i
        res = ~(res & y) & ~(~res & ~y)
        y += i
        res = (res & ~y) | (~res & y)
        y += i
        res = (res | y) & (~res | ~y)
        enc_flag += chr(res)
        enc_flag=enc_flag[::-1]
        i += 1
    return enc_flag

open('encrypted','w').write(enc(open('flag.txt').read().strip(),open('key.txt').read().strip()))
