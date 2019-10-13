def padding(plane_text):
    pt_l = len(plane_text)
    if pt_l == 50:
        return plane_text
    else:
        plane_text += "%" * (50 - pt_l)
        return plane_text


def decrypt(mes, enc):
    res = ""
    for idx in range(0, 50):
        m = mes[idx]
        e = enc[idx * 2: (idx + 1) * 2]
        res_num = ord(m) ^ int(e, 16)
        res += chr(res_num)
    return res


def main():
    enc = "1030183e1a3e0230180b301a262b1b003c020915310e3a0d3a1a1139181b1137031a1a385a4d407a5640465740517a4e405c"
    plane_text = padding("I_may_lose_my_secret_key_before_long.")
    key = decrypt(plane_text, enc)
    print(key)
    flag_enc = "140e1c3b020a0b1c3f28142e3001370e311f1b3e1a0d3a2b0610152d160a000d1d1c072b1d0b16001c033c2a2a26224e405c"
    flag = decrypt(key, flag_enc)
    print(flag)


if __name__ == "__main__":
    main()
