import pickle
import io

payload = b'\x8c\x08builtins\x8c\x07getattr\x93\x942\x8c\x08builtins\x8c\x05input\x93\x8c\x06FLAG> \x85R\x8c\x06encode\x86R)R\x940g0\n\x8c\x08builtins\x8c\x04dict\x93\x8c\x03get\x86R\x8c\x08builtins\x8c\x07globals\x93)R\x8c\x01f\x86R\x8c\x04seek\x86R\x94g0\n\x8c\x08builtins\x8c\x03int\x93\x8c\x07__add__\x86R\x940g0\n\x8c\x08builtins\x8c\x03int\x93\x8c\x07__mul__\x86R\x940g0\n\x8c\x08builtins\x8c\x03int\x93\x8c\x06__eq__\x86R\x940g3\ng5\n\x8c\x08builtins\x8c\x03len\x93g1\n\x85RM@\x00\x86RM\x05\x01\x86R\x85R.0g0\ng1\n\x8c\x0b__getitem__\x86R\x940M\x00\x00\x940g2\ng3\ng0\ng6\ng7\n\x85R\x8c\x06__le__\x86RM\x7f\x00\x85RMJ\x01\x86R\x85R.0g2\ng3\ng4\ng5\ng3\ng7\nM\x01\x00\x86Rp7\nM@\x00\x86RMU\x00\x86RM"\x01\x86R\x85R0g0\ng0\n]\x94\x8c\x06append\x86R\x940g8\n\x8c\x0b__getitem__\x86R\x940g0\n\x8c\x08builtins\x8c\x03int\x93\x8c\nfrom_bytes\x86R\x940M\x00\x00p7\n0g9\ng11\ng6\n\x8c\x08builtins\x8c\x05slice\x93g4\ng7\nM\x08\x00\x86Rg4\ng3\ng7\nM\x01\x00\x86RM\x08\x00\x86R\x86R\x85R\x8c\x06little\x86R\x85R0g2\ng3\ng4\ng5\ng3\ng7\nM\x01\x00\x86Rp7\nM\x08\x00\x86RMw\x00\x86RM\xc9\x01\x86R\x85R0g0\n]\x94\x8c\x06append\x86R\x940g0\ng12\n\x8c\x0b__getitem__\x86R\x940g0\n\x8c\x08builtins\x8c\x03int\x93\x8c\x07__xor__\x86R\x940I1244422970072434993\n\x940M\x00\x00p7\n0g13\n\x8c\x08builtins\x8c\x03pow\x93g15\ng10\ng7\n\x85Rg16\n\x86RI65537\nI18446744073709551557\n\x87R\x85R0g14\ng7\n\x85Rp16\n0g2\ng3\ng4\ng5\ng3\ng7\nM\x01\x00\x86Rp7\nM\x08\x00\x86RM\x83\x00\x86RM\xa7\x02\x86R\x85R0g0\ng12\n\x8c\x06__eq__\x86R(I8215359690687096682\nI1862662588367509514\nI8350772864914849965\nI11616510986494699232\nI3711648467207374797\nI9722127090168848805\nI16780197523811627561\nI18138828537077112905\nl\x85R.'

f = io.BytesIO(payload)
res = pickle.load(f)

if isinstance(res, bool) and res:
    print("Congratulations!!")
else:
    print("Nope")
