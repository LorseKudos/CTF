def calc_base(_c):
    c = bin(_c)[2:]
    while len(c) % 8 != 4:
        c = '0' + c
    c = c[:64]
    m = int.from_bytes(b'CakeCTF{', 'little')
    m = bin(m)[2:]
    assert(len(m) == 63)
    r = ''
    for i in range(63):
        r = str(int(c[i])^int(m[-(i+1)])) + r
    return r

def LFSR_call(_r, bitlength):
    r = _r
    r_ls = []
    for i in range(bitlength):
        r_ls.append(r & 1)
        b = (r & 1) ^\
            ((r & 2) >> 1) ^\
            ((r & 8) >> 3) ^\
            ((r & 16) >> 4)
        r = (r >> 1) | (b << 63)
    return r_ls

def decrypt(_c, ls):
    c = bin(_c)[2:]
    while len(c) % 8 != 4:
        c = '0' + c
    assert(len(c) == len(ls))
    m = ''
    for i in range(len(c)):
        m += str(int(c[i])^ls[i])
    return int(m[::-1], 2).to_bytes(len(ls)//8+1, 'little')

c = 0x58566f59979e98e5f2f3ecea26cfb0319bc9186e206d6b33e933f3508e39e41bb771e4af053

def main(c):
    r = calc_base(c)
    r1 = int('0' + r, 2)
    r2 = int('1' + r, 2)

    r_ls1 = LFSR_call(r1, (c.bit_length()//8)*8+4)
    r_ls2 = LFSR_call(r2, (c.bit_length()//8)*8+4)

    print(decrypt(c, r_ls1))
    print(decrypt(c, r_ls2))

main(c)
