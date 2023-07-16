from Crypto.Util.number import long_to_bytes
from sympy.ntheory import factorint

encs = ((0xf0d3, 0x2350f23a0dff, 0xfe4c025c5f4),
        (0x85f, 0x32d18e9d4d33, 0x1b792ff17e8a),
        (0x8e63, 0x3866cd71f1b, 0x183b156ab40),
        (0x8249, 0x10ae9be3fc8f, 0xbeffcf5e5da),
        (0xc6a1, 0x9d942eff67d, 0x297cf86e251),
        (0xc6d, 0x01de2e3aa8bb1, 0xeb3edc1d4b4),
        (0xaef5, 0x103fc65841f3, 0xfa10ce3a08),
        (0xd5df, 0x11a0970edc9, 0x2bdd418672),
        (0xe68d, 0x5f8d20bddf39, 0x5ebb5050ea46),
        (0xf3fb, 0x45b14e11e0ed, 0x5bf9b73cf86))
flag = b""
print(encs)
for e, n, c in encs:
    print(e, n, c)
    factors = factorint(n)
    print(factors)
    phi = 1
    for factor in factors:
        phi *= factor - 1

    d = pow(e, -1, phi)
    m = pow(c, d, n)
    m = long_to_bytes(m)
    print(m[::-1])
    flag += m[::-1]
print(flag)
