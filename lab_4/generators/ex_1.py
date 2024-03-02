#Create a generator that generates the squares of numbers up to some number N.

def func(n):
    for i in range(n+1):
        yield i**2

n = 5
for i in func(n):
    print(i)