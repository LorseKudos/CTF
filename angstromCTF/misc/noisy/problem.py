import numpy as np
from random import gauss
# morse = REDACTED
# repeats = REDACTED
morse = ".."
repeats = 4
pointed = []
for c in morse:
    if c == ".":
        pointed.extend([1 for x in range(10)])
    if c == "-":
        pointed.extend([1 for x in range(20)])
    if c == " ":
        pointed.extend([0 for x in range(20)])
    pointed.extend([0 for x in range(10)])

print(pointed)

for _ in range(repeats):
    signal = pointed
    output = []
    for x, bit in enumerate(signal):
        output.append(bit + gauss(0, 2))

    signal = list(np.array(output) - .5)
    print('\n'.join([str(x) for x in signal])+"\n")
