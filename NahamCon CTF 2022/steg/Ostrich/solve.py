from PIL import Image
from apng import APNG

orig_filename = "ostrich.jpg"
orig_image = Image.open(orig_filename)
pixels = orig_image.load()
print(pixels)
width, height = orig_image.size

for png, _ in APNG.open("result.apng").frames:
    png.save(f"result.png")
    enc_image = Image.open("result.png")
    c = "?"
    print("hoge")

    for x in range(width):
        print("1")

        for y in range(height):
            enc_pixel = enc_image.getpixel((x, y))
            orig_pixel = orig_image.getpixel((x, y))
            if abs(enc_pixel[0] - orig_pixel[0]) + abs(enc_pixel[1] - orig_pixel[1]) \
                    + abs(enc_pixel[2] - orig_pixel[2]) > 20 and orig_pixel[2] != 0 \
                    and enc_pixel[2] < 3:

                c_enc = enc_pixel[0] * 256 + enc_pixel[1]
                c_flag = c_enc // orig_pixel[2]
                c = chr(c_flag)
                print(c, orig_pixel, enc_pixel, c_enc % orig_pixel[2])

                c_enc = enc_pixel[0]
                c_flag = c_enc // orig_pixel[2]
                c = chr(c_flag)
                print(c, orig_pixel, enc_pixel, c_enc % orig_pixel[2])
    enc_image.close()
