
'''

Types of Function in Python 

basic functions
Normal Function 
lambda function
args function
kwargs function (keyword argument function)

'''

# find circle areas and circumference

# if parameter is not pass it should return default value 

import math

def circle_data(radius = 5):
    area = math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius
    return area , circumference


# destructure return function returns

input_radius = int(input('Enter the Radius of Circle = '))

circle_area , circle_circumference = circle_data(input_radius)

print('Area of Circle =',round(circle_area,2),'Circumference of Circle = ',round(circle_circumference,2))


# if argument is not submitted by user then it will take default paramter

def enroll_user(username = 'Harry'):
    # print('Enrolled User = ', username)
    return username

enrol_user_data1 = enroll_user()             #argument is not provided
enrol_user_data2 = enroll_user('Darsh')      #argument is pass

# print('Enrolled User Name is ',enrol_user_data1)
# print('Enrolled User Name is ',enrol_user_data2)



# Lambda Function 
'''
this is useful to create function which is used for temporary period of only one time
lambda function is to reduce memory space for single time used function it has great use case in python framework like flask and django

A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.

so lets learn with example of creatting lambda function for finding cube

syntax 

variable = lambda parameter: logic expression

'''

print('\n  lambda function ')


cube = lambda x: x ** 3

# print('lambda() = ',cube(9))



'''
(*args) function it is a special function which will help you perform operation of multiple parameter input of function denoted with (*args)

'''

# Get multiple paramter as input and return sum of them

print('\n  *args function ')


def sum_of_all(*args):
    sum = 0
    for i in args:
        sum = sum + i
    
    return sum


sum1 = sum_of_all(2,3,4,5)
sum2 = sum_of_all(2,3,4,5,6,7,8)
sum3 = sum_of_all(2,3,4,5,45,7,8,184,84,846,4)

# print(sum1, sum2, sum3)


'''
(**kwargs) function are keyword arguments fucntion it help you to perform operation on multiple dictionary  key value pair

'''

print('\n  **kwargs function ')

def business_team(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} : {value}')

team1 = business_team(Darshan = 'Full Stack Developer', Sagar = 'SEO Specialist', Rohan = 'UIUX Designer', Rohit = 'Android App Developer' )

# print(team1)


# python fizzBuzz 

def FizzBuzz(num):
    if (num % 3 != 0 and num % 5 != 0):
        print(num)
    elif (num % 3 == 0 and num % 5 == 0):
        print('FizzBuzz')    
    elif (num % 3 == 0 ):
        print('Fizz')
    elif (num % 5 == 0):
        print('Buzz')
    else:
        print('Invalid Number')

number = int(input(' Enter the Number to check Divisibility of 3, 5 or both = '))

# FizzBuzz(number)


'''

The yield keyword is used to return a list of values from a function.

Unlike the return keyword which stops further execution of the function, the yield keyword continues to the end of the function.

When you call a function with yield keyword(s), the return value will be a list of values, one for each yield.

Use the return keyword to return only one value, and stop further execution.

inspite of return we use yeild keyword to fetch function values

'''


# if we used return keyword

def even_generator(limit):
    for i in range(2,limit + 1, 2):
        # print(i)
        return i

return_value = even_generator(16)
print('return = ',return_value)

def even_generator2(limit):
    for i in range(2,limit + 1, 2):
        yield i

# yield_value = even_generator2(15)

# print('yield =', yield_value)

for num in even_generator2(16):
    print(num)


# type 2

def function_list():
    yield 'Darshan'
    yield 'Full Stack Developer'
    yield 'Coder, Youtuber, Teacher, and Explorer.'


for skills in function_list():
    print(skills)


# recurssive functions 

'''
Recurrsive function are the function in which we call function in same function

'''


def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


fact_interger_val = int(input('Enter Input Number = '))

factorial_value = factorial(fact_interger_val)

print('Factorial = ', factorial_value)









