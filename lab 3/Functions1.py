'''
#ex1
def gram_to_ounces(gramms):
    ounces = 28.3495231 * gramms
    return ounces

gramm = int(input("Enter the amount in grams: "))
print(gram_to_ounces(gramm))

#ex2
def temperature(fahrenheit):
    centigrade = ((fahrenheit - 32) * 5) / 9
    return centigrade

temp = int(input("Enter the temperature in Fahrenheit: "))
print(temperature(temp))

#ex3
def solve(numheads, numlegs):
    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens

        if (2 * num_chickens + 4 * num_rabbits) == numlegs:
            return num_chickens, num_rabbits

    return None

numheads = 35
numlegs = 94

result = solve(numheads, numlegs)

if result:
    chickens, rabbits = result
    print(f"Number of chickens: {chickens}")
    print(f"Number of rabbits: {rabbits}")
else:
    print("No solution found.")

#ex4
    def is_prime(num):
    if num<2:
        return False
    else:
        for i in range(2,int(num**0.5)+1):
           if num%i==0:
               return False
        return True
def filter_prime(numbers):
    return[num for num in numbers if is_prime(num)]

List_of_numbers=input("print numbers which separated by space: ")
Numbers=[int(num) for num in List_of_numbers.split()]

prime_numbers=filter_prime(Numbers)

print("changed list: ",prime_numbers)

#ex5
from itertools import permutations

def print_permutations(input_string):

    perms = permutations(input_string)


    for perm in perms:
        print(''.join(perm))

user_input = input("Enter a string: ")
print_permutations(user_input)

#ex6
def reverse_sentence(sentence):
    words=sentence.split()
    reversed_sentence=' '.join(reversed(words))

    return reversed_sentence

input_string=input("enter a string: ")
new_sentence=reverse_sentence(input_string)

print("new reversed string is: ",new_sentence)

#ex7
def check_for_similarity(List):
    for i in range(len(List)-1):
        if List[i]==3 and List[i+1]==3:
            return True

Numbers=input("enter list of numbers: ")
Numbers_list=[int(num) for num in Numbers.split()]
if check_for_similarity(Numbers_list):
    print("True")
else:
    print("False")

#ex8
    def check_for_order(List):
    for i in range(len(List)-2):
        if List[i]==0 and List[i+1]==0 and List[i+2]==7:
            return True

Numbers=input("enter list of numbers: ")
Numbers_list=[int(num) for num in Numbers.split()]
if check_for_order(Numbers_list):
    print("True")
else:
    print("False")

#ex9
def volume_of_sphere(Radius):
    volume=((Radius**3)*4*3.14)/3
    return volume

radius_of_sphere=int(input("enter the size of radius: "))
print("volume equal to: ",volume_of_sphere(radius_of_sphere))

#ex10
def unique_list(List):
    Unique=[]

    for element in List:
        if element not in Unique:
            Unique.append(element)
    return Unique

example_input = input("Enter a list of numbers: ")
example_list = [int(num) for num in example_input.split()]
answer = unique_list(example_list)

print("first list",example_list)
print("unique list",answer)

#ex11
def palindrome(input_string):
    check="".join(reversed(input_string))

    if check==input_string:
        return True
    else:
        return False

example_string=input("print a string: ")
if palindrome(example_string):
    print("True")
else:
    print("False")

#ex12
def histogram(input_list):
    answer_string = ""
    for element in input_list:
        while element > 0:
            answer_string += "*"
            element -= 1
        answer_string += " "
    return answer_string

example_input = input("Enter a list of numbers separated by spaces: ")
the_list = [int(num) for num in example_input.split()]
answer = histogram(the_list)

print("The result is:", answer)

#ex13
def guess_number(number):
    secret_number = 9

    if number > secret_number:
        print("Your guess is too high")
    elif number < secret_number:
        print("Your guess is too low")
    else:
        return True

name = input("Hello! What is your name?")
print("Well,", name, "I am thinking of a number between 1 and 20.")

num = int(input("Take a guess."))
counter_of_guesses = 0

while not guess_number(num):
    counter_of_guesses += 1
    num = int(input("Take a guess."))

print("Good job, ", name, "! You guessed my number in ", counter_of_guesses, " guesses!")
'''
