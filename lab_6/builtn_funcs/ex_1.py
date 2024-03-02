#Write a Python program with builtin function to multiply all the numbers in a list
import functools

lst = [1,2,3,4,5]

res = functools.reduce(lambda x,y: x*y, lst)
print(res)
