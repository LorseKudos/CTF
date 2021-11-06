from functools import reduce


def XOR(*X):
    xor = lambda A, B: bytes(x ^ y for x, y in zip(A, B))
    return reduce(xor, X)


ciphertext = bytes.fromhex("bd35b1c95ee9436db8fad5c3aa493660e606fa4dd7fe171aac75313c18ce5fcf86f0")
A = bytes.fromhex("cae61858ee8c7198632c652fd8416092eb165e2f847f0ebd80637ed0ffd96c6e0359")
B = bytes.fromhex("e6ed8bda14f67343d81830f0f2be3299a97b541db48cfa1873a13e8d774f1e243ce7")
C = bytes.fromhex("319fe8d6cb01539bbcb9ef9f13663d8b6274c50b0ce578c94b7910b3ca785ccea8d4")

print(XOR(ciphertext, A, C))
