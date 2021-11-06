import base64


def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])


token = base64.b64decode("3lYXJmbOzlu+Fx2ebBBg8msDsXV8W06naE8TKyM0xDsuqTr3tl4R1PQBDIrxzKDHMHAw7nXr6QindZYqnT8uvg==")

iv, enc_data = token[:16], token[16:]

origin = b'{"admin": false,'
goal = b'{"admin": true, '

print(iv)
goal_iv = b""
goal_iv = byte_xor(iv, byte_xor(origin, goal))

print(goal_iv)

token = base64.b64encode(goal_iv + enc_data)
print(token)
