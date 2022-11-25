import base64
import json

from pwn import *

def get_ciphertext():
    while True:
        r.sendline(json.dumps({"msg": "request"}).encode())
        json_res = json.loads(r.recvline())
        if "ciphertext" in json_res:
            return base64.b64decode(json_res["ciphertext"])


len_flag = 20
r = remote('socket.cryptohack.org', 13370)

r.recvline()

candidates = [set(range(32,127)) for _ in range(len_flag)]

while any(map(lambda x: len(x) != 1, candidates)):
    ciphertext = get_ciphertext()
    for i in range(len_flag):
        candidates[i].discard(ciphertext[i])

print(candidates)
print("".join(list(map(lambda x: chr(x.pop()), candidates))))
