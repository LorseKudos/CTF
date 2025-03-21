enc = [8215359690687096682, 1862662588367509514, 8350772864914849965, 11616510986494699232,
       3711648467207374797, 9722127090168848805, 16780197523811627561, 18138828537077112905]
n = 18446744073709551557
e = 65537

d = pow(e, -1, n-1)

xor_key = 1244422970072434993
for idx, c in enumerate(enc):
    m = pow(c, d, n)
    assert pow(m, e, n) == c
    m = m ^ xor_key
    xor_key = c
    print(m.to_bytes(8, byteorder="little").decode(), end="")
