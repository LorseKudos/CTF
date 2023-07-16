s = "Fcn_yDlvaGpj_Logi}eias{iaeAm_s"

flag = [""]*len(s)
for i in range(len(s)):
    flag[i * 7 % 30] = s[i]

print("".join(flag))
