from pwn import *
import os



if __name__ == '__main__':
    # context.log_level = 'debug'
    r = remote('misc.ctf.zer0pts.com', 10001)

    flag = 'zer0pts{s1gn+|3xp^|fr4c.}'

    len_flag = 24

    key = b""
    for c in flag:
        key += bytes([0x100 - ord(c)])

    print(key.hex())

    for i in range(0x20, 0x7f):

        r.recvuntil(b"Key: ")
        r.sendline((key + bytes([0x100 - i]) + b"\x00" *
                   (len_flag - len(flag))).hex())

        hash = r.recvline().split()[1]

        print(f"{chr(i)}: {hash}")

            # if b'0x3' in hash:
            #     flag += chr(0x100 - i)
            #     key += bytes([i])
            #     print(flag)
            #     break
