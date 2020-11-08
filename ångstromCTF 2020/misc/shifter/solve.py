import socket
import re

from functools import lru_cache


@lru_cache(maxsize=1000)
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)


def get_ans(p, n):
    rot = fibonacci(n)
    p = (chr((ord(c) - ord('A') + rot) % 26 + ord('A')) for c in p)

    return ''.join(p)


def recvuntil(s, tail):
    data = ''
    while True:
        if tail in data:
            return data
        data += s.recv(1).decode('utf-8')


if __name__ == '__main__':

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('misc.2020.chall.actf.co', 20300))
    while True:
        receivedata = s.recv(1024).decode('utf-8')
        print("[+]receivedata=", receivedata)
        pattern = r'''Shift (.*) by n=(.*)'''
        p, n = re.findall(pattern, receivedata)[0]

        ans = get_ans(p, int(n))
        print("[+]ans=", ans)
        senddata = str(ans)
        print("[+]senddata=", senddata)
        s.sendall((senddata+"\n").encode("utf-8"))
