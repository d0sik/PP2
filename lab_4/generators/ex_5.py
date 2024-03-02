#Implement a generator that returns all numbers from (n) down to 0.

def func(n):
    for i in range(n, -1, -1):
        yield i

for i in func(10):
    print(i)
