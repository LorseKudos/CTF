with open('output.txt', 'r') as f:
    plaintext = bytes.fromhex(f.read())
    print(plaintext)

for key in range(256):
    ciphertext = [key ^ byte for byte in plaintext]
    print(bytes(ciphertext))
