import zlib
flag_compressed = b'x\x9c\xcb,\xca,N.I\xab\xce\xa8,H-\xca\xcc\xcf\x8b7,\x8e\xcf3(\x89O\x8c/3.\xaa\x8cO70H\x897HJ+5M6)1(R\xac\x05\x00\xce\xff\x11\xdb'
flag = zlib.decompress(flag_compressed)
print(flag)
# irisctf{hyperion_1s_n0t_a_v3ry_g00d_0bfu5c4t0r!}
