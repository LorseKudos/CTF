from Crypto.Util.number import bytes_to_long, inverse, long_to_bytes
from pwn import *
import hashlib
import base64

enc = "33c7461caec455639a2c78889df87b2b787ed5c63954b411c12f2306190bb676164d382d3b0976bd56bf827e770dbe1ac2d4a53f38d83a1b4cf782f97a51929d2f591d46af0b7a40f714d9145f78d07d"
byte_enc = bytes.fromhex(enc)

print((byte_enc[:32] + byte_enc[48:]).hex())
