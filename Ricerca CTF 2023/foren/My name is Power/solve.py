# $ python3 vol.py -f /mnt/c/Users/Lorse/Desktop/memory/memory.raw  --key
#
# Last Write Time Hive Offset     Type    Key     Name    Data    Volatile
# -       0x850e68a85000  Key     ?\Software\Microsoft\CTF        -      -
# -       0x850e68a5b000  Key     ?\Software\Microsoft\CTF        -      -
# -       0x850e68b32000  Key     ?\Software\Microsoft\CTF        -      -
# -       0x850e6a450000  Key     ?\Software\Microsoft\CTF        -      -
# -       0x850e6b01e000  Key     ?\Software\Microsoft\CTF        -      -
# -       0x850e7287b000  Key     ?\Software\Microsoft\CTF        -      -
# -       0x850e71680000  Key     ?\Software\Microsoft\CTF        -      -
# -       0x850e72355000  Key     ?\Software\Microsoft\CTF        -      -
# -       0x850e71aca000  Key     ?\Software\Microsoft\CTF        -      -
# -       0x850e71657000  Key     ?\Software\Microsoft\CTF        -      -
# -       0x850e7165e000  Key     ?\Software\Microsoft\CTF        -      -
# -       0x850e727c0000  Key     ?\Software\Microsoft\CTF        -      -
# -       0x850e71ac8000  Key     ?\Software\Microsoft\CTF        -      -
# -       0x850e70d46000  Key     ?\Software\Microsoft\CTF        -      -
# -       0x850e722d5000  Key     ?\Software\Microsoft\CTF        -      -
# -       0x850e71de5000  Key     ?\Software\Microsoft\CTF        -      -
# -       0x850e6da1c000  Key     ?\Software\Microsoft\CTF        -      -
# -       0x850e6ef8d000  Key     ?\Software\Microsoft\CTF        -      -
# -       0x850e6ee07000  Key     ?\Software\Microsoft\CTF        -      -
# -       0x850e6edf0000  Key     ?\Software\Microsoft\CTF        -      -
# -       0x850e6eded000  Key     ?\Software\Microsoft\CTF        -      -
# -       0x850e6ec63000  Key     ?\Software\Microsoft\CTF        -      -
# -       0x850e6ec5f000  Key     ?\Software\Microsoft\CTF        -      -
# -       0x850e6ec5c000  Key     ?\Software\Microsoft\CTF        -      -
# -       0x850e6eda2000  Key     ?\Software\Microsoft\CTF        -      -
# -       0x850e6ede2000  Key     ?\Software\Microsoft\CTF        -      -
# -       0x850e6eb98000  Key     ?\Software\Microsoft\CTF        -      -
# -       0x850e6e835000  Key     ?\Software\Microsoft\CTF        -      -
# -       0x850e6e83f000  Key     ?\Software\Microsoft\CTF        -      -
# -       0x850e6e274000  Key     ?\Software\Microsoft\CTF        -      -
# 2023-04-01 08:44:57.000000      0x850e6e280000  Key     \??\C:\Users\User\ntuser.dat\Software\Microsoft\CTF     Assemblies              False
# 2023-04-01 08:44:57.000000      0x850e6e280000  Key     \??\C:\Users\User\ntuser.dat\Software\Microsoft\CTF     DirectSwitchHotkeys            False
# 2023-04-01 08:44:57.000000      0x850e6e280000  Key     \??\C:\Users\User\ntuser.dat\Software\Microsoft\CTF     HiddenDummyLayouts             False
# 2023-04-01 08:44:57.000000      0x850e6e280000  Key     \??\C:\Users\User\ntuser.dat\Software\Microsoft\CTF     SortOrder               False
# 2023-04-01 08:44:57.000000      0x850e6e280000  Key     \??\C:\Users\User\ntuser.dat\Software\Microsoft\CTF     TIP             False
# 2023-04-01 08:44:57.000000      0x850e6e280000  REG_BINARY      \??\C:\Users\User\ntuser.dat\Software\Microsoft\CTF     fiend   "
# 39 da 2a 85 c9 5b 42 17 9.*..[B.
# 84 11 d8 23 3b 0b f2 0e ...#;...
# 26 8c 95 89 ff e6 f1 7e &......~
# 4b f8 43 42 d0 24 37 70 K.CB.$7p"       False
# -       0x850e6dcd2000  Key     ?\Software\Microsoft\CTF        -      -
# 2023-04-19 00:23:03.000000      0x850e6b6e3000  Key     \??\C:\Windows\ServiceProfiles\LocalService\NTUSER.DAT\Software\Microsoft\CTF   Assemblies              False
# 2023-04-19 00:23:03.000000      0x850e6b6e3000  Key     \??\C:\Windows\ServiceProfiles\LocalService\NTUSER.DAT\Software\Microsoft\CTF   DirectSwitchHotkeys             False
# 2023-04-19 00:23:03.000000      0x850e6b6e3000  Key     \??\C:\Windows\ServiceProfiles\LocalService\NTUSER.DAT\Software\Microsoft\CTF   SortOrder               False
# 2023-04-19 00:23:03.000000      0x850e6b6e3000  Key     \??\C:\Windows\ServiceProfiles\LocalService\NTUSER.DAT\Software\Microsoft\CTF   TIP    False


from Crypto.Cipher import AES
enc_fiend = b"\x39\xda\x2a\x85\xc9\x5b\x42\x17\x84\x11\xd8\x23\x3b\x0b\xf2\x0e\x26\x8c\x95\x89\xff\xe6\xf1\x7e\x4b\xf8\x43\x42\xd0\x24\x37\x70"

key = b"\xd3\xa8\xbf\x38\x75\x91\xee\x55\xbc\xbb\x59\x28\x24\x50\x32\xe1\x9b\x38\x1e\x77\xd3\x13\x47\xad\x0d\x95\xd1\xbd\xc0\x98\x68\x8c"
iv = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'
cipher = AES.new(key, AES.MODE_CBC, iv)
fiend = cipher.decrypt(enc_fiend)
xor_key = [102, 49, 98, 98, 51, 114]

for i in range(len(fiend)):
    print(chr(fiend[i] ^ xor_key[i % len(xor_key)]), end="")
# RicSec{6r347_90w3r!}
