#Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
n = int(input())
def func(n):
    for i in range(n+1):
        if not i%3 and not i%4:
            yield i

for i in func(n):
    print(i)
