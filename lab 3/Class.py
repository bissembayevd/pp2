'''
#ex1
class upperString:

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print("String in upper case:", self.input_string.upper())


upperString = upperString()
upperString.getString()
upperString.printString()

#ex2
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length * self.length

k=int(input("Write the length of square:"))

square = Square(k)
print("Area of square with length :",k," is ", square.area())

#ex3
#import math

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")

    def move(self,new_x,new_y):
        self.x=new_x
        self.y=new_y

    def distance(self,second_point):
        dx = self.x - second_point.x
        dy = self.y - second_point.y
        distance=(dx**2+dy**2)**0.5
        return distance

point1=Point(3,4)
point2=Point(6,9)

point1.show()
point2.show()

distance_between=point1.distance(point2)
print(f"Distance between two points: {distance_between}")

point1.move(1,2)
point1.show()

#ex4
class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Withdrawal denied.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")


account = BankAccount("John Doe", 1000)

account.deposit(500)
account.withdraw(200)
account.withdraw(800)
account.withdraw(1000)

#ex5
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


numbers = [2, 5, 8, 11, 13, 16, 17, 19, 23, 29]


prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Original list:", numbers)
print("Prime numbers:", prime_numbers)
'''
