#Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
n = int(input())
def func(n):
    for i in range(n+1):
        if not i%2:
            yield i

for i in func(n):
    print(i, end=', ')