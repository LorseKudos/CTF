import socket
import re
import base64


if __name__ == '__main__':

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('cha.hackpack.club', 41715))

    receivedata = s.recv(1024).decode('utf-8')
    pattern = r'''=> (.*)\n'''
    enc_flag = base64.b64decode(re.findall(pattern, receivedata)[0])

    senddata = "\x00"*58
    s.sendall((senddata+"\n").encode("utf-8"))
    receivedata = s.recv(1024).decode('utf-8')
    session_key = base64.b64decode(re.findall(pattern, receivedata)[0])

    print(''.join(chr(x ^ y) for (x, y) in zip(enc_flag, session_key)))
