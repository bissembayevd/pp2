'''
#ex1
import re
def check_pattern(pattern):
   x=re.search(r"ab*",pattern)
   if x:
     print("we have a match")
   else:
     print("not match")
example="abb"
check_pattern(example)

#ex2
import re
def check_pattern(pattern):
    x=re.search(r"abb",pattern)
    y=re.search(r"abbb",pattern)

    if x or y:
        print("we have a match")
    else:
        print("not match")

example_1 = "abb"
example_2 = "abbb"
example_3 = "ab"
check_pattern(example_1)
check_pattern(example_2)
check_pattern(example_3)

#ex3
import re
def check_pattern(pattern):
    check=re.compile(r"[a-z]+_[a-z]+")
    x=check.findall(pattern)
    if x:
        print(f'Sequences found: {", ".join(x)}')
    else:
        print("No sequences found")

example_string = "i_am_Kaisar and i want_to be an_engineer"
check_pattern(example_string)


#ex4
import re
def check_pattern(pattern):
    check=re.compile(r"[A-Z]+[a-z]+")
    x=check.findall(pattern)

    if x:
        print(f'Sequences found: {", ".join(x)}')
    else:
        print("no sequence found")

example_string = "Kaisar is going to be New leader of Kazakh youngSters"
check_pattern(example_string)



#ex5
import re
def check_pattern(pattern):
    x=re.search(r"^a.*b$",pattern)
    if x:
        print("matches")
    else:
        print("not a match")

example_string = "ascdnvjcbxb"
check_pattern(example_string)


#ex6
import re
def replace_characters(pattern):
    new_string = re.sub(r'[ ,.]',':',pattern)
    print(new_string)

test_string = "almaty is beautiful,unique city with big history."
replace_characters(test_string)


#ex7
import re
def snake_to_camel(snake_case):
    words = re.split('_',snake_case)
    camel_case = words[0] + ''.join(word.capitalize() for word in words[1:])
    print(camel_case)

test_string = "i_enjoy_programming_but_i_am_lazy"
snake_to_camel(test_string)


#ex8
import re
def split_string(pattern):
    result = re.split(r'(?=[A-Z])', pattern)
    result.pop(0)
    print(result)

test_string = "Almaty is very Beautiful city"
split_string(test_string)


#ex9
import re
def insert_spaces(string):
    new_string = re.sub(r'([a-z])([A-Z])',r'\1 \2',string)
    print(new_string)

example_string = "tableAndfood"
insert_spaces(example_string)


#ex10
import re
def camel_to_snake(string):
    snake_case = re.sub(r'([a-z])([A-Z])',r'\1_\2',string)
    return snake_case.lower()


example_string = "almatyBigCity"
result=camel_to_snake(example_string)
print(result)
'''
