#!/usr/local/bin/python -u

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.strxor import strxor
from more_itertools import ichunked

BLOCK = AES.block_size


def main():
    enc_flag = bytes.fromhex(
        "4d6a0450a09f14e4ded179f6b8d9d08756711d56b0ab06e9ded165ecabd3ebb0405a1f5bb48301d9e39122acf5d1d6ef403d4c06be9047b2fca5169ecab2b3df")
    enc_key = bytes.fromhex("35156425cbe4629691b20189dda5a4c8")
    enc_key = strxor(enc_key, b"\x10"*16)

    pt = pad(enc_flag, BLOCK)
    ct = b''
    for bk in ichunked(pt, BLOCK):
        ct += strxor(enc_key, bytes(bk))

    print(ct)


if __name__ == '__main__':
    main()
