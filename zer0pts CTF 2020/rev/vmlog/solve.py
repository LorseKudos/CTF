import string

ans = ""

check_mem = [4588277794174371330, 4557362566608270193, 4597225827500493308, 4399455111035409631, 3664679811648746944, 1822527803964528750, 2107290073593614393, 103104307719214561, 3773217954610171964, 1852072839260827083, 3465871536121230779, 223194874355517702, 1454204952931951837, 3030456872916287478, 426011771323652532, 1276028785627724173, 1962653697352394735, 1600956848133034570, 2045579747554458289, 4248193240456187641, 4478689482975263576, 1235692576284114044, 2579703272274331094, 1394874119223018380, 4275420194958799226, 2401030954359721279, 1313700932660640339, 2401701271938149070, 4217153612451355368, 2389747163516760623, 3483955087661197897, 4522489230881850831]

for i in range(len(check_mem)):
    for char in string.printable:
        check_cnt = 0
        reg = 0
        mem = [0 for _ in range(10)]
        p = 0
        pc = 0
        buf = ""

        program = "+s+>s>++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[s<<l>*<s>>l-]<<l-s>l*-s*-s*-s*-s*-s*-s>l*+++++s*-----s****s>>l+s[Ml-s<<l>,[<<*>>s<<<l>>>%<s>>l<s>l+s<l]>l]<<lp"

        while pc < len(program):
            op = program[pc]

            if op == "+":
                reg += 1
            elif op == "-":
                reg -= 1
            elif op == "*":
                reg *= mem[p]
            elif op == "%":
                reg = mem[p] % reg
            elif op == "l":
                reg = mem[p]
            elif op == "s":
                mem[p] = reg
            elif op == ">":
                p = (p + 1) % 10
            elif op == "<":
                p = (p - 1) % 10
            elif op == ",":
                if check_cnt == i + 1:
                    a = char
                else:
                    a = ans[check_cnt - 1]
                if not a:
                    reg = 0
                else:
                    reg += ord(a)
            elif op == "p":
                buf += str(reg)
            elif op == "[":
                if reg == 0:
                    cnt = 1
                    while cnt != 0:
                        pc += 1
                        if program[pc] == "[":
                            cnt += 1
                        if program[pc] == "]":
                            cnt -= 1
            elif op == "]":
                if reg != 0:
                    cnt = 1
                    while cnt != 0:
                        pc -= 1
                        if program[pc] == "[":
                            cnt -= 1
                        if program[pc] == "]":
                            cnt += 1
            elif op == "M":
                check_cnt += 1
                if check_cnt == i + 2:
                    if mem[2] == check_mem[i]:
                        ans += char
                    break

            pc += 1

print(ans)
