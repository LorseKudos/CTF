import socket
import re


def get_ans(d, t):
    h, m, s = map(int, t.split(':'))
    seconds_per_mile = (h * 3600 + m * 60 + s) / d
    m, s = int(seconds_per_mile // 60), int(seconds_per_mile % 60)
    return f'{m}:{s}'


def recvuntil(s, tail):
    data = ''
    while True:
        if tail in data:
            return data
        data += s.recv(1).decode('utf-8')


if __name__ == '__main__':

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('ctf.umbccd.io', 5300))
    receivedata = s.recv(1024).decode('utf-8')
    print("[+]receivedata=", receivedata)
    while True:
        receivedata = s.recv(1024).decode('utf-8')
        print("[+]receivedata=", receivedata)
        pattern = r'''I ran (.*) in (.*) What's my pace\?'''
        distance, time = re.findall(pattern, receivedata)[0]

        ans = get_ans(float(distance), time)
        senddata = str(ans)
        print("[+]senddata=", senddata)
        s.sendall((senddata+"\n").encode("utf-8"))
