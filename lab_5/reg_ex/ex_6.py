import re

def func(string):
    return re.findall(r"[A-Z][a-z]*", string)


