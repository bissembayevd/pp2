'''
#ex1.Create a generator that generates the squares of numbers up to some number N.
def generate_func(n):
    x=n
    k=1
    while n>=k:
        yield k**2
        k+=1

l=int(input("enter any number: "))
output=generate_func(l)
for num in output:
    print(num)

#ex2.Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
    def generate_func(n):
    x=n
    k=0
    while n>=k:

        yield k
        k+=2

l=int(input("enter any number: "))
output=generate_func(l)
for num in output:
    print(num)

#ex3.Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
    def generate_func(n):
    x=n
    k=12
    while n>=k:

        yield k
        k+=12

l=int(input("enter any number: "))
output=generate_func(l)
for num in output:
    print(num)

#ex4.Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
    import math
def generate_func(n,m):
    x=n
    y=m
    while x<=m:
        if math.isqrt(x) ** 2 == x:
            yield x

        x+=1

l=int(input("enter the start of interval: "))
j=int(input("enter the end of interval: "))
output=generate_func(l,j)
for num in output:
    print(num)

#ex5.Implement a generator that returns all numbers from (n) down to 0.
    def generate_func(n):
        x=n
        while x>=0:
          print(x)
          x-=1

z=int(input("enter the number"))
generate_func(z)
'''
