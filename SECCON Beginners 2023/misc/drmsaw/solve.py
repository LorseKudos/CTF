from Crypto.Cipher import AES

iv = b"\x00"*16
key =bytes([99, 9, 61, 110, 94, 114, 119, 194, 42, 163, 63, 8, 97, 114, 131, 41])

cipher = AES.new(key, AES.MODE_CBC, iv)
enc = b""
for i in range(3):
    with open(f"./public/videos/video{i}.ts", "rb") as f_in:
        enc = f_in.read()
    with open(f"./video{i}.ts", "wb") as f_out:
        f_out.write(cipher.decrypt(_enc))

# ffmpeg -i "concat:video0.ts|video1.ts|video2.ts" -c copy -bsf:a aac_adtstoasc -movflags +faststart output.mp4
# ctf4b{d1ff1cul7_70_3n5ur3_53cur17y_1n_cl13n7-51d3-4pp5}
