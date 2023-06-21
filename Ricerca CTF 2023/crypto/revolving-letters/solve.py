LOWER_ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def decrypt(secret, key):
    assert len(secret) <= len(key)

    result = ""
    for i in range(len(secret)):
        # Don't encode symbols and capital letters (e.g. "A", " ", "_", "!", "{", "}")
        if secret[i] not in LOWER_ALPHABET:
            result += secret[i]
        else:
            result += LOWER_ALPHABET[(LOWER_ALPHABET.index(secret[i]) -
                                      LOWER_ALPHABET.index(key[i])) % 26]

    return result


flag_encrypted = "RpgSyk{qsvop_dcr_wmc_rj_rgfxsime!}"
key = "thequickbrownfoxjumpsoverthelazydog"
flag = decrypt(flag_encrypted, key)

print(flag)
