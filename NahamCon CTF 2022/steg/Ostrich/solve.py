from PIL import Image
from apng import APNG

orig_filename = "ostrich.jpg"
orig_image = Image.open(orig_filename)
pixels = orig_image.load()
width, height = orig_image.size

flag = ""

for png, _ in APNG.open("result.apng").frames:
    png.save(f"result.png")
    enc_image = Image.open("result.png")

    for x in range(width):
        for y in range(height):
            enc_pixel = enc_image.getpixel((x, y))
            orig_pixel = orig_image.getpixel((x, y))
            if enc_pixel[2] == 0 and orig_pixel[2] != 0:
                if enc_pixel[1] != orig_pixel[1]:
                    c_enc = enc_pixel[0] * 256 + enc_pixel[1]
                else:
                    c_enc = enc_pixel[0]
                c_flag = c_enc // orig_pixel[2]
                c = chr(c_flag)
                flag += c
                print(c, orig_pixel, enc_pixel)
    enc_image.close()

print(flag)
