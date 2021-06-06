import string
import collections


data = open("output.txt", "rb").read().decode().split(" ")

def encrypt(word, key):
    shifts = [ord(k) - ord('a') for k in key]
    pt = [ord(c) - ord('a') for c in word]
    return ''.join([chr(((p - shifts[i]) % len(string.ascii_lowercase)) + ord('a')) for i, p in enumerate(pt)])


def encrypt_data(data, key):
    return " ".join([encrypt(word, key) for word in data])


word = "polyalphabetic"

enc = "wvoafooxtcpktm"

key = ""
for i in range(14):
    key += chr((ord(enc[i]) - ord(word[i])) % 26 + ord('a'))

msg = encrypt_data(data, key)
if msg[:2] == 'if':
    print(key, word)
    print(msg)
    print()
