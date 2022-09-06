with open('output.txt') as f:
    ciphertext = f.read()

characters = set(ciphertext) - {'\n'}
print(characters)
replacement = {
    "\n": "\n",
    "h": "h",
    "w": "o",
    "f": "p",
    "y": "e",
    "A": "{",
    "u": "}",
    "B": ".",
    "\"": "a",
    "S": "n",
    "d": "d",
    "s": "c",
    "l": "u",
    "i": "l",
    "k": "t",
    "T": "_",
    "M": "g",
    "g": " ",
    "t": "y",
    "q": "i",
    ",": "x",
    ".": "r",
    "V": "v",
    "}": "m",
    "c": "f",
    "_": "s",
    "j": "b",
    " ": "w",
    "p": "O",
    "r": "s",
    "a": "B",
    "o": "A",
    "e": "q",
    "v": "M",
    "{": "T",
    "b": "\"",
    "x": "I",
    "O": "V",
    "n": "E",
    "E": "k",
    "I": "j"
}

plaintext = ''.join(replacement.get(c, "~") for c in ciphertext)
print(plaintext)
