import re

def func(string):
    pattern = r"ab*"
    if re.fullmatch(pattern, string):
        return True
    else:
        return False

