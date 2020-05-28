import socket
import re

from functools import lru_cache


def get_ans(p, n):
    rot = fibonacci(n)
    p = (chr((ord(c) - ord('A') + rot) % 26 + ord('A')) for c in p)

    return ''.join(p)


def recvuntil(s, tail):
    data = ''
    while True:
        if tail in data:ｎ
            return data
        data += s.recv(1).decode('utf-8')


if __name__ == '__main__':

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('rsacalc.quals.beginners.seccon.jp', 10001))
    while True:
        receivedata = s.recv(1024).decode('utf-8')
        print("[+]receivedata=", receivedata)
        pattern = r'''N: (.*)\n'''
        N = int(re.findall(pattern, receivedata)[0])
        print(N)

        s.sendall(("2\n").encode("utf-8"))

        receivedata = s.recv(1024).decode('utf-8')
        print("[+]receivedata=", receivedata)

        ans = get_ans(p, int(n))
        print("[+]ans=", ans)
        senddata = str(ans)
        print("[+]senddata=", senddata)
        s.sendall((senddata+"\n").encode("utf-8"))
