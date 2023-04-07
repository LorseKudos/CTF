from pwn import *
import string
from itertools import product

if __name__ == "__main__":
    if args.REMOTE:
        context.log_level = 'debug'
        r = remote("stretchy.chal.irisc.tf", 10704)
        r.recvuntil("with:\n")
        pow_cmd = r.recvline().strip().decode()
        r.recvuntil("? ")

        print(pow_cmd)
        pow_ans = input().strip()
        r.sendline(pow_ans.encode())
    else:
        # r = process("python3 server.py", shell=True)
        pass

    for password in product(string.hexdigits[:16], repeat=2):
        password = "".join(password[0]*64 + password[1]*8)
        print(r.recvuntil("> "))
        r.sendline(password.encode())

    r.interactive()
# irisctf{truncation_silent_and_deadly}
