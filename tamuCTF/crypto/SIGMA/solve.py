key = '10320831141252164475480592397410881183128414021520157116851780189419421991209921942315241625302578269728072902300131153236334834643575368637343782389340044129'

flag = "g"

i = 3
interval = 3

prev_num = 103

while i < len(key):
    num = int(key[i:i + interval])

    if num - prev_num < 0:
        interval += 1
        num = int(key[i:i + interval])

    flag += chr(num - prev_num)
    print(flag)
    prev_num = num
    i += interval
