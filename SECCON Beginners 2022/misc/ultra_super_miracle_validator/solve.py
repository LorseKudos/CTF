from z3 import *

x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40 =\
    Bools(["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8", "x9", "x10", "x11", "x12", "x13", "x14", "x15", "x16", "x17", "x18", "x19", "x20", "x21", "x22", "x23", "x24", "x25", "x26", "x27", "x28", "x29", "x30", "x31", "x32", "x33", "x34", "x35", "x36", "x37", "x38", "x39", "x40"])
s = Solver()

P1  = Or(x1, x6, x12, Not(x21), x32) # ($x1 or $x6 or $x12 or not $x21 or $x32) and
P2  = Or(x3, x5, Not(x11), x24, x35) # ($x3 or $x5 or not $x11 or $x24 or $x35) and
P3  = Or(Not(x3), x31, x40, x9, x27) # (not $x3 or $x31 or $x40 or $x9 or $x27) and
P4  = Or(x4, x8, x10, x29, x40) # ($x4 or $x8 or $x10 or $x29 or $x40) and
P5  = Or(x4, x7, x11, x25, Not(x36)) # ($x4 or $x7 or $x11 or $x25 or not $x36) and
P6  = Or(x8, x14, x18, x21, x38) # ($x8 or $x14 or $x18 or $x21 or $x38) and
P7  = Or(x12, x15, Not(x20), x30, x35) # ($x12 or $x15 or not $x20 or $x30 or $x35) and
P8  = Or(x19, x21, Not(x32), x33, x39) # ($x19 or $x21 or not $x32 or $x33 or $x39) and
P9  = Or(x2, x37, x19, Not(x23)) # ($x2 or $x37 or $x19 or not $x23) and
P10 = Or(Not(x5), x14, x23, x30) # (not $x5 or $x14 or $x23 or $x30) and
P11 = Or(Not(x5), x8, x18, x23) # (not $x5 or $x8 or $x18 or $x23) and
P12 = Or(x33, x22, x4, x38) # ($x33 or $x22 or $x4 or $x38) and
P13 = Or(x2, x20, x39) # ($x2 or $x20 or $x39) and
P14 = Or(x3, x15, Not(x30)) # ($x3 or $x15 or not $x30) and
P15 = Or(x6, Not(x17), x30) # ($x6 or not $x17 or $x30) and
P16 = Or(x8, x29, Not(x21)) # ($x8 or $x29 or not $x21) and
P17 = Or(Not(x16), x1, x29) # (not $x16 or $x1 or $x29) and
P18 = Or(x20, x10, Not(x5)) # ($x20 or $x10 or not $x5) and
P19 = Or(Not(x13), x25) # (not $x13 or $x25) and
P20 = Or(x21, x28, x30) # ($x21 or $x28 or $x30) and
P21 = Not(x2) # not $x2 and
P22 = x3 # $x3 and
P23 = Not(x7) # not $x7 and
P24 = Not(x10) # not $x10 and
P25 = Not(x11) # not $x11 and
P26 = x14 # $x14 and
P27 = Not(x15) # not $x15 and
P28 = Not(x22) #  not $x22 and
P29 = x26 # $x26 and
P30 = Not(x27) # not $x27 and
P31 = x34 # $x34 and
P32 = x36 # $x36 and
P33 = x37 # $x37 and
P34 = Not(x40) # not $x40
s.add((And(P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, P13, P14, P15, P16, P17, P18, P19, P20, P21, P22, P23, P24, P25, P26, P27, P28, P29, P30, P31, P32, P33, P34)))
r = s.check()
if r == sat:
  m = s.model()
  print(m)

"""
[x14 = True,
 x4 = True,
 x3 = True,
 x34 = True,
 x20 = True,
 x21 = True,
 x37 = True,
 x26 = True,
 x36 = True,
 x12 = True,
 x31 = True,
 x8 = True]
"""

x = [
  "dummy",
  "e3 82 89 e3 81 9b e3 82 93 e9 9a 8e e6 ae b5",
  "e3 82 ab e3 83 96 e3 83 88 e8 99 ab",
  "e5 bb 83 e5 a2 9f e3 81 ae e8 a1 97",
  "e3 82 a4 e3 83 81 e3 82 b8 e3 82 af e3 81 ae e3 82 bf e3 83 ab e3 83 88",
  "e3 83 89 e3 83 ad e3 83 ad e3 83 bc e3 82 b5 e3 81 b8 e3 81 ae e9 81 93",
  "e7 89 b9 e7 95 b0 e7 82 b9",
  "e3 82 b8 e3 83 a7 e3 83 83 e3 83 88",
  "e5 a4 a9 e4 bd bf",
  "e7 b4 ab e9 99 bd e8 8a b1",
  "e7 a7 98 e5 af 86 e3 81 ae e7 9a 87 e5 b8 9d",
  "82 e7 82 b9 82 f1 8a 4b 92 69",
  "83 4a 83 75 83 67 92 8e",
  "94 70 9a d0 82 cc 8a 58",
  "83 43 83 60 83 57 83 4e 82 cc 83 5e 83 8b 83 67",
  "83 68 83 8d 83 8d 81 5b 83 54 82 d6 82 cc 93 b9",
  "93 c1 88 d9 93 5f",
  "83 57 83 87 83 62 83 67",
  "93 56 8e 67",
  "8e 87 97 7a 89 d4",
  "94 e9 96 a7 82 cc 8d 63 92 e9",
  "30 89 30 5b 30 93 96 8e 6b b5",
  "30 4b 30 76",
  "5e c3 58 9f 30 6e 88 57",
  "30 a4 30 c1 30 b8 30 af 30 6e 30 bf 30 eb 30 c8",
  "30 c9 30 ed 30 ed 30 fc 30 b5 30 78 30 6e 90 53",
  "72 79 75 70 70 b9",
  "30 b8 30 e7 30 c3 30 c8",
  "59 29 4f 7f",
  "7d 2b 96 7d 82 b1",
  "79 d8 5b c6 30 6e 76 87 5e 1d",
  "2b 4d 49 6b 2d 2b 4d 46 73 2d 2b 4d 4a 4d 2d 2b 6c 6f 34 2d",
  "2b 4d 45 73 2d 2b 4d 48",
  "2b 58 73 4d 2d 2b 57 4a 38 2d 2b 4d 47 34 2d 2b",
  "2b 4d 4b 51 2d 2b 4d 4d 45 2d 2b 4d 4c 67 2d 2b 4d 4b 38 2d 2b 4d 47 34 2d 2b 4d 4c 38 2d 2b 4d",
  "2b 4d 4d 6b 2d 2b 4d 4f 30 2d 2b 4d 4f 30 2d 2b 4d 50 77 2d 2b 4d 4c 55 2d 2b 4d 48 67 2d 2b 4d",
  "2b 63 6e 6b 2d 2b 64 58 41 2d 2b 63",
  "2b 4d 4c 67 2d 2b 4d 4f 63 2d 2b 4d 4d 4d 2d 2b",
  "2b 57 53 6b 2d 2b 54 33",
  "2b 66 53 73 2d 2b 6c 6e 30 2d 2b 67",
  "2b 65 64 67 2d 2b 57 38 59 2d 2b 4d 47 34 2d 2b 64 6f 63 2d"]

for i in [14, 4, 3, 34, 20, 21, 37, 26, 36, 12, 31, 8]:
# for i in [13, 20, 32, 16, 17, 5]:
  tmp = ""
  for c in x[i].split():
    tmp += f"0x{c}, "
  tmp += "0x00"
  print(f"char d{i}[] = {{{tmp}}}; ", end="")
