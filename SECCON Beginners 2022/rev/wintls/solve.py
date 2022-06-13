str1 = "c4{fAPu8#FHh2+0cyo8$SWJH3a8X"
str2 = "tfb%s$T9NvFyroLh@89a9yoC3rPy&3b}"

flag = ""

idx1 = idx2 = 0
for i in range(len(str1 + str2)):
    if i % 3 == 0 or i % 5 == 0:
        flag += str1[idx1]
        idx1 += 1
    else:
        flag += str2[idx2]
        idx2 += 1

print(flag)
