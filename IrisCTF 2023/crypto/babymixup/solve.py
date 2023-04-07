from Crypto.Cipher import AES

IV1 = bytes.fromhex("4ee04f8303c0146d82e0bbe376f44e10")
CT1 = bytes.fromhex("de49b7bb8e3c5e9ed51905b6de326b39b102c7a6f0e09e92fe398c75d032b41189b11f873c6cd8cdb65a276f2e48761f6372df0a109fd29842a999f4cc4be164")
IV2 = bytes.fromhex("1fe31329e7c15feadbf0e43a0ee2f163")
CT2 = bytes.fromhex("f6816a603cefb0a0fd8a23a804b921bf489116fcc11d650c6ffb3fc0aae9393409c8f4f24c3d4b72ccea787e84de7dd0")

message = b"Hello, this is a public message. This message contains no flags."
cipher = AES.new(IV1, AES.MODE_CBC, message[:16])
key = cipher.decrypt(CT1[:16])

cipher = AES.new(IV1, AES.MODE_CBC, key)
assert cipher.encrypt(message) == CT1

cipher = AES.new(key, AES.MODE_CBC, IV2)
flag = cipher.decrypt(CT2)
print(flag)
# irisctf{the_iv_aint_secret_either_way_using_cbc}
