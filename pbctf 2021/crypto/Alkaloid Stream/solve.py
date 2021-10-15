#!/usr/bin/env python3
def xor(a, b):
    return [x ^ y for x, y in zip(a, b)]


def recover_keystream(key, public):
    st = set(key)
    keystream = []
    for v0, v1 in public:
        if v0 in st:
            keystream.append(0)
        elif v1 in st:
            keystream.append(1)
        else:
            assert False, "Failed to recover the keystream"
    return keystream

def bytes_to_bits(inp):
    res = []
    for v in inp:
        res.extend(list(map(int, format(v, '08b'))))
    return res


def bits_to_bytes(inp):
    res = []
    for i in range(0, len(inp), 8):
        res.append(int(''.join(map(str, inp[i:i+8])), 2))
    return bytes(res)


enc = "cd4c1a7edd7a421dcea72ae8bf47946d74f6cdba763a6a052a3f2955333dc6fa267f5297c405bf807e922380ebf9628194bf319e8ae4074dc5476de1d81a52d72c29f0e8b590ac8f6a78bb"
with open("output.txt") as f:
    public = eval(f.readlines()[1])

ln = len(public)

key = [0]*ln
searched = set()

for i in range(ln):
    fake = 0
    for j in range(ln // 3):
        if (ln - i) + j >= ln:
            break
        fake ^= key[(ln - i) + j]

    for j in range(ln):
        if j in searched:
            continue
        if public[j][0] == fake:
            key[-i-1] = public[j][1]
            searched.add(j)
        if public[j][1] == fake:
            key[-i-1] = public[j][0]
            searched.add(j)


keystream = recover_keystream(key, public)
enc = bytes_to_bits(bytes.fromhex(enc))
print(bits_to_bytes(xor(enc, keystream)))
