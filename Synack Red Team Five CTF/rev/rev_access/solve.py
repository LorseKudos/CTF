enc = b"L\x13T\x7fME\x7f\x11N\x7fL\x13T\x7fMEEEE\x7fIN\x01\x01"

for e in enc:
    print(chr(e ^ 0x20), end="")
