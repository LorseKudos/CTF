import socket
import re


def get_ans(*scores):
    scores = list(scores)
    for i in range(len(scores)):
        if scores[i] == 'love':
            scores[i] = 0
        elif not scores[i].isdigit():
            scores[i] = 100
        print(scores[i])
        scores[i] = int(scores[i])
    print(scores)
    return 0 if scores[0] > scores[1] else 1


def recvuntil(s, tail):
    data = ''
    while True:
        if tail in data:
            return data
        data += s.recv(1).decode('utf-8')


if __name__ == '__main__':

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('arthurashe.ctf.umbccd.io', 8411))
    receivedata = s.recv(1024).decode('utf-8')
    print("[+]receivedata=", receivedata)
    s.sendall(("Y\n").encode("utf-8"))
    i = 1
    flag = ""
    try:
        while True:
            print(f"[+]Challenge {i}")
            receivedata = s.recv(1024).decode('utf-8')
            print("[+]receivedata=", receivedata)
            pattern = r'''The result of this .* is (.*)-(.*).'''
            score_1, score_2 = re.findall(pattern, receivedata)[0]

            ans = get_ans(score_1, score_2)
            senddata = str(ans)
            print("[+]senddata=", senddata)
            s.sendall((senddata+"\n").encode("utf-8"))
            flag += senddata
            i += 1
    except Exception:
        receivedata = s.recv(1024).decode('utf-8')
        print("[+]receivedata=", receivedata)
        print(flag)
