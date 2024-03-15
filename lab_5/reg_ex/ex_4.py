import re

def func(string):
    pattern = r"a.+b"
    if re.fullmatch(pattern, string):
        return True
    else:
        return False
