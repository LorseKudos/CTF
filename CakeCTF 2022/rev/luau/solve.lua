key = "CakeCTF 2022"
xored = {62, 85, 25, 84, 47, 56, 118, 71, 109, 0, 90, 71, 115, 9, 30, 58, 32, 101, 40, 20, 66, 111, 3, 92, 119, 22, 90, 11, 119, 35, 61, 102, 102, 115, 87, 89, 34, 34} -- 38個

flag_enc = {}
key_enc = {67, 97, 107, 101, 67, 84, 70, 32, 50, 48, 50, 50}

for i = 1, #xored, 1 do
    L10_2 = i - 1
    L11_2 = #key_enc
    L10_2 = L10_2 % L11_2
    L10_2 = 1 + L10_2
    L9_2 = xored[i] ~ key_enc[L10_2]
    flag_enc[i] = L9_2
end

rev = {}
for i = #flag_enc, 1, -1 do
	rev[#rev+1] = flag_enc[i]
end
flag_enc = rev

flag = ""
for i = 1, #flag_enc do
    flag = flag .. string.char(flag_enc[i])
end
print(flag)

-- CakeCTF{w4n1w4n1_p4n1c_uh0uh0_g0ll1r4}
