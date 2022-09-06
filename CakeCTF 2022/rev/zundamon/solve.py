
with open("dump", "rb") as f:
    dumps = f.readlines()

scan_code = {
    2: "1",
    3: "2",
    4: "3",
    5: "4",
    6: "5",
    7: "6",
    8: "7",
    9: "8",
    10: "9",
    11: "0",
    16: "q",
    17: "w",
    18: "e",
    19: "r",
    20: "t",
    21: "y",
    22: "u",
    23: "i",
    24: "o",
    25: "p",
    26: "@",
    27: "[",
    30: "a",
    31: "s",
    32: "d",
    33: "f",
    34: "g",
    35: "h",
    36: "j",
    37: "k",
    38: "l",
    44: "z",
    45: "x",
    46: "c",
    47: "v",
    48: "b",
    49: "n",
    50: "m",
    51: ",",
    52: ".",
    53: "/",
    54: "\\",
    57: " ",
    42: "[shift]",
    89: "[→]"
}
flag = False
for dump in dumps:
    if flag:
        if int(dump[0]) != 42 and not dump[2]:
            flag = False
            continue
        key = scan_code.get(int(dump[0]), "?")
        print(int(dump[0]), key, dump[2])
        flag = False
    if dump.startswith(b"$3"):
        flag = True

# CakeCTF{b3_c4r3ful_0f_m4l1c10us_k3yl0gg3r}
