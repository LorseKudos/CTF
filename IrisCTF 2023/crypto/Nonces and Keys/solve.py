from Crypto.Cipher import AES


def xor(a, b):
    return bytes(aa ^ bb for aa, bb in zip(a, b))


with open("challenge_enc.sqlite3", "rb") as f:
    enc_db = f.read()

sqlite_signature = b'SQLite format 3\x00'

key = bytes.fromhex("13371337133713371337133713371337")
iv = xor(enc_db[:16], sqlite_signature)
cipher = AES.new(key, AES.MODE_OFB, iv)

db = sqlite_signature + cipher.decrypt(enc_db[16:])

with open("challenge.sqlite3", "wb") as f:
    f.write(db)
# irisctf{g0tt4_l0v3_s7re4mciph3rs}
