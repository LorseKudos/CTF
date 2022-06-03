from Crypto.Cipher import AES


def decrypt(data, password):
    return AES.new(password, AES.MODE_ECB).decrypt(data)


with open("db.encrypted", "rb") as f:
    data = f.read()

for i in range(10**4):
    password = str(f"{i:04}")*4

    try:
        db = decrypt(data, password.encode())
        if b"content" in db:
            print(db)
            break
    except ValueError:
        pass
