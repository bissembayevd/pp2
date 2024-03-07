'''
#ex1.Write a Python program to convert degree to radian.
import math

degree=int(input("Input degree: "))

def converter(n):
    x=(n*3.14)/180
    return x

output=converter(degree)
print("Output radian: ",output)

#ex2.Write a Python program to calculate the area of a trapezoid.
height=int(input("enter the height: "))
base_1=int(input("enter the first base: "))
base_2=int(input("enter the second base: "))

x=((base_1+base_2)/2)*height
print("the area of trapezoid: ",x)

#ex3.Write a Python program to calculate the area of regular polygon.
sides=int(input("number of sides: "))
length=int(input("length of the side: "))
output=pow(length,2)
print("area equivalent to: ",output)

#ex4.Write a Python program to calculate the area of a parallelogram.
base=int(input("length of base: "))
height=int(input("height of parallelogramm: "))
print("expected output: ",length*base)
'''
