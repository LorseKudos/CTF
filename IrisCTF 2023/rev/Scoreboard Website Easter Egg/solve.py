categories = ['Binary Exploitation', 'Cryptography', 'Forensics', 'Miscellaneous',
              'Networks', 'Radio Frequency', 'Reverse Engineering', 'Web Exploitation', 'Welcome']

expected_h = [
    0x2b47,
    0x2ec76,
    0x31e0f8,
    0x34ffd37,
    0x384feac4,
    0x3bd4ea3c3,
    0x3f9238ecb2,
    0x438b5c7e540,
    0x47c412466529,
    0x4c40536acd1d6,
    0x510458a17a1b46,
    0x56149e2b91bfcc8,
    0x5b75e80e4adbe365,
    0x12d468f2f89a4375,
    0x401af822823e94e2,
    0x41ca7a4aa6280cc2,
    0x5e721ef508a904f2,
    0x45940e4593396e2f,
    0x9ed4f29ec6d07adf,
    0x8c241c8b33d8358e,
]


def calc(category):
    return ord(category[1]) * ord(category[6]) - ord(category[3])


prev_b = 23
cnt = 0
for b in expected_h:
    for category in categories:
        _b = ((prev_b * 17) + calc(category)) & 0xffffffffffffffff
        if _b == b:
            cnt += 1
            print(cnt, category)
    prev_b = b
# irisctf{ponies_who_eat_rainbows_and_poop_butterflies}
