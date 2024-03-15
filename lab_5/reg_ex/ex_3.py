import re

def func(string):
    pattern = r'[A-Z][a-z]+'
    sequences = re.findall(pattern, string)
    return sequences
