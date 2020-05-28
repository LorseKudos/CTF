import socket
import base64
from string import ascii_uppercase
from math import gcd
from itertools import cycle, chain


def fence_pattern(rails, size):
    zig_zag = cycle(chain(range(rails), range(rails - 2, 0, -1)))
    return zip(zig_zag, range(size))


def rail_decode(msg, rails):
    fence = fence_pattern(rails, len(msg))
    fence_msg = zip(msg, sorted(fence))
    return ''.join(
        char for char, _ in sorted(fence_msg, key=lambda item: item[1][1]))


def affine_decode(msg, a, b, m=26):
    upper = ascii_uppercase
    if gcd(a, 26) != 1:
        raise ValueError('a and 26 are not coprime. Please try again.')
    out = ''
    n = 1
    count = 1
    while True:
        if a*n > m*count:
            if a*n == (m*count) + 1:
                break
            count += 1
        n += 1
    for char in msg:
        if char.isalpha():
            d = int((n*(upper.index(char) - b)) % m)
            out += upper[d]
        else:
            out += char
    return out


def caesar(s, n):
    d = {}
    for c in (65, 97):
        for i in range(26):
            d[chr(i+c)] = chr((i+n) % 26 + c)

    return "".join([d.get(c, c) for c in s])

def get_ans(enc):
    print(enc)
    if enc.startswith("QbtrPGS"):
        return caesar(enc, 13)
    if enc.startswith("TewuSJV"):
        return caesar(enc, 10)
    if enc.startswith("RG9nZUNU"):
        return base64.b64decode(enc).decode()
    if enc.startswith("IRXWOZKDKRD"):
        return base64.b32decode(enc).decode()
    if enc.startswith("446F6765435446"):
        return base64.b16decode(enc).decode()
    if enc.startswith("WLTVXGU"):
        table = str.maketrans(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "ZYXWVUTSRQPONMLKJIHGFEDCBA")
        return enc.translate(table)
    if enc.startswith("HCIQYVZ"):
        return affine_decode(enc, 9, 6)
    return rail_decode(enc, 3)


def recvuntil(s, tail):
    data = ''
    while True:
        if tail in data:
            return data
        data += s.recv(1).decode('utf-8')


if __name__ == '__main__':

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('ctf.umbccd.io', 5200))
    receivedata = recvuntil(
        s, '\n-----------------------------------------------------------------------\n')
    print("[+]receivedata=", receivedata)
    i = 1
    while i < 110:
        print(f"[+]Challenge {i}")
        receivedata = s.recv(1024).decode('utf-8')
        print("[+]receivedata=", receivedata)

        ans = get_ans(receivedata.strip())
        print("[+]senddata=", ans)
        s.sendall((ans+"\n").encode("utf-8"))
        i += 1
