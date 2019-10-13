from PIL import Image
from Crypto.Cipher import AES
import os
import codecs

base = os.path.dirname(os.path.abspath(__file__))
name = os.path.normpath(os.path.join(base, 'problem.png'))
img = Image.open(name)
# 画像サイズ
width, height = img.size
# 答え表示用
img2 = Image.new('RGB', (width, height))

# 各ピクセルのRGB値取得
ls = ''
for h in range(height):
    for w in range(width):
        pixel = list(img.getpixel((w, h)))
        # Rの値. 16進表記で1桁なら0補完
        if len(hex(pixel[0])[2:]) == 2:
            ls += hex(pixel[0])[2:]
        else:
            ls += '0' + hex(pixel[0])[2:]
        # Gの値
        if len(hex(pixel[1])[2:]) == 2:
            ls += hex(pixel[1])[2:]
        else:
            ls += '0' + hex(pixel[1])[2:]
        # Bの値
        if len(hex(pixel[2])[2:]) == 2:
            ls += hex(pixel[2])[2:]
        else:
            ls += '0' + hex(pixel[2])[2:]

print("pick up RGB values.")

# byte列変換
byte = codecs.decode(('%x' % int(ls, 16)), 'hex_codec')

# ECBの復号
key = b'this_a_secretkey'
cipher = AES.new(key, AES.MODE_ECB)
byte = cipher.decrypt(byte)

print("decryption finished.")

# RGB値セット
for h in range(height):
    for w in range(width):
        img2.putpixel((w, h), (byte[3 * (w + h * width)],
                               byte[3 * (w + h * width) + 1],
                               byte[3 * (w + h * width) + 2]))

# 表示
img2.show()
