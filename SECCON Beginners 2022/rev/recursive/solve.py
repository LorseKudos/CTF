# flagは38文字
# 入力文字列を前半・後半に分けてそれぞれcheck
# a

table = ["a"]*2000
def check(param1, param2):
    length = len(param1)

    if length == 1:
        print(param1, param2)
    else:
        half_length = length // 2
        part_param1 = param1[:half_length]
        res = check(part_param1, param2)
        part_param1 = param1[half_length:]
        res = check(part_param1, half_length * half_length + param2)


check("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKL" ,0)

# a 0 
# b 1
# c 4
# d 5
# e 16
# f 17
# g 20
# h 21
# i 22
# j 81
# k 82
# l 85
# m 86
# n 87
# o 106
# p 107
# q 110
# r 111
# s 112
# t 361
# u 362
# v 365
# w 366
# x 377
# y 378
# z 381
# A 382
# B 383
# C 442
# D 443
# E 446
# F 447
# G 448
# H 467
# I 468
# J 471
# K 472
# L 473
