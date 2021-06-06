from pwn import *
import hashlib
import base64

r = remote('fiend.zajebistyc.tf', 17002)

flag = "flat{"

timestamp = r.recvline().decode().strip()
print(timestamp)
IV = ORIGIN_IV = hashlib.md5(timestamp.encode('ascii')).digest()


def xor(message, iv):
    return bytes([_a ^ _b for _a, _b in zip(message, iv)])


for _ in range(16 - len(flag)):
    ORIGIN_IV = IV
    r.recvuntil(":\n")

    msg = "A" * (15 - len(flag))
    send = base64.b64encode(msg.encode()).decode()
    r.sendline(send)
    goal_enc = r.recvline().decode().strip()
    IV = hashlib.md5(IV).digest()
    for i in range(33, 126):
        r.recvuntil(":\n")

        msg = "A" * (15 - len(flag)) + flag + chr(i)
        send = base64.b64encode(xor(xor(msg.encode(), IV), ORIGIN_IV)).decode()

        r.sendline(send)
        enc = r.recvline().decode()
        IV = hashlib.md5(IV).digest()
        if enc[:20] == goal_enc[:20]:
            flag += chr(i)
            print(flag)
            break

print(flag)
