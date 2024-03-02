#Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters

st = input()

def count_lower(s):
    count = 0
    for i in s:
        if i.islower():
            count += 1
    return count

def count_upper(s):
    count = 0
    for i in s:
        if i.isupper():
            count += 1
    return count


l_letters = count_lower(st)

u_letters = count_upper(st)

print(f"Lower letters: {l_letters}", f"upper_letters: {u_letters}", sep='\n')