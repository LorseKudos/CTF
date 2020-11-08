import socket
import subprocess
import binascii


def encodeHex(s):
    enc = ''
    xcode = ''
    for i in range(len(s)):
        if s[i] == '\\' and len(xcode) == 0:
            xcode += s[i]
        elif s[i] == 'x' and len(xcode) == 1:
            xcode += s[i]
        elif len(xcode) == 2:
            xcode += s[i]
        elif len(xcode) == 3:
            xcode += s[i]
            enc += xcode[2:]
            xcode = ''
        else:
            enc += '%02x' % ord(s[i])
    return enc


def LEA(cmd):
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ret = proc.stdout.decode('utf-8').split('\n')
    token = ret[0].encode('utf-8')
    init = ret[1][:1].encode('utf-8')
    lines = ret[1][1:].split(';')
    encHex = encodeHex(lines[0])
    pad = binascii.unhexlify(encHex)
    append = (';' + lines[1]).encode('utf-8')
    data = init + pad + append

    return (token, data)


def recvuntil(s, tail):
    data = ''
    while True:
        if tail in data:
            return data
        data += s.recv(1).decode('utf-8')


if __name__ == '__main__':

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('challenges.tamuctf.com', 8812))

    salt_len = 1
    init_key = '1'
    init_hash = 'a17b713167841563563ac6903a8bd44801be3c0fb81b086a4816ea457f8c829a6d5d785b49161972b7e94ff9790d37311e12b32221380041a99c16d765e8776c'
    append_key = ';0000000000000000000000000000000000000000000000001'

    cmd_format = ['hashpump', '-s', init_hash, '-d',
                  init_key, '-k', 'salt_len', '-a', append_key]

    receivedata = s.recv(1024).decode('utf-8')
    print("[+]receivedata=", receivedata)

    while True:
        s.sendall(("2\n").encode("utf-8"))
        receivedata = s.recv(1024).decode('utf-8')
        print("[+]receivedata=", receivedata)

        cmd_format[6] = str(salt_len)

        crack_hash, crack_key = LEA(cmd_format)

        s.send(crack_key + b'\n')
        receivedata = s.recv(1024).decode('utf-8')
        print("[+]receivedata=", receivedata)

        s.send(crack_hash + b'\n')
        print("[+]salt_len=", salt_len)
        receivedata = s.recv(1024).decode('utf-8')
        print("[+]receivedata=", receivedata)

        if('gigem' in receivedata):
            break
        salt_len += 1
