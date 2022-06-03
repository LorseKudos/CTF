ct = open('out', 'r').read()

for k in range(0, 0xFFFD):
    pt = ''
    for c in ct:
        pt += chr((ord(c) - k) % 0xFFFD)
    if pt.startswith('flag'):
        print(pt)
        break
