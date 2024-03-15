import re

def func(string):
    pattern = r'[ ,.]'
    replaced_string = re.sub(pattern, ':', string)
    return replaced_string
