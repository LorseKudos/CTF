from email.encoders import encode_base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

with open('encrypted.bin', 'rb') as f:
	enc = f.read()

with open('privatekey.pem','r') as f:
	key = RSA.import_key(f.read())

cipher_rsa = PKCS1_OAEP.new(key)
flag = cipher_rsa.decrypt(enc)

print(flag)
