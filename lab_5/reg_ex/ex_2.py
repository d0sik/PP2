import re

def func(string):
    pattern = r"ab{2,3}"
    if re.fullmatch(pattern, string):
        return True
    else:
        return False
