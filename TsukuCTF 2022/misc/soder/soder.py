#!/usr/bin/env python3
import os
import re
from timeout_decorator import timeout

FLAG = os.getenv("FLAG", "TsukuCTF22{dummy_flag}")

@timeout(5)
def flag_validator(pattern):
    re.match(pattern, FLAG)

def yakitori():
    pattern = input("Pattern: ")
    print("I check your pattern.")
    try:
        # This function will be timed out in 5 seconds.
        flag_validator(pattern)
    except:
        pass
    print("Probably valid flag!")

yakitori()