#!/usr/bin/env python3

greet = "Hartelĳk welkom! De sleutel is ".encode()
print(len(greet))
enc = bytes.fromhex("d8f3fa74e5ffedf7eb3a7fef6cfb6f7ff9f2ec75e0ffede5f77e7def68f97772fcfaee32e1fffff5e73a7fef6dfc6777f8f3bb71f1fffde7b73a7fbb78fd3572fcf2ed7ee0ffede5f77e79ef68fc757bfcf6a878f8ffffd7eb7b5fbf6dfc375efbffee30f2fffdf5d37f79cf7ff93577dff3bc7efffffdf7b37f59bb7aff3f7fffffae")

for i in range(32):
    print(greet[i], enc[i])
    assert greet[i] & enc[i] == greet[i]

# key =
print(enc)

for i in range(16):
    assert key[i] | greet[i] == enc[i]
