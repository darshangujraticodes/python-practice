
'''
Python Loops
'''

# Sum of Number Problem Statement 1

print('\nSum of Number')

input_val = int(input('Enter your number = '))

def sum_of_num(number):
    sum = 0
    while (number > 0):
        rem = int(number % 10)
        sum = sum + rem
        number = int(number / 10)   
    
    return sum

print('Sum of Input Number = ', sum_of_num(input_val))


# Reverse of Number Problem Statement 2

print('\nReverse of Number')

 
def reverse_of_num(number):
    rem = 0
    rev = 0
    while (number > 0):
        rem = number % 10
        rev = (rev * 10) + rem
        number = int(number / 10)
    
    return rev

print('Reverse of Input Number = ', reverse_of_num(input_val))


# Multiplication Table printer Problem Statement 3

print('\nMaths Table of Number')

number = int(input('Enter the Number to get Multiplication = '))
def maths_table(number):
    for i in range(1,11):
        print(number," * ",i,' = ',number * i)

maths_table(number)

print('\nMaths Table of Number')


# Reverse of String Problem Statement 3

print('\nPrint String value in Reverse order !')


input_string = input('Enter your String Value = ')
rev_string = ''
str = []

for char in input_string:
    rev_string = char + rev_string

print(rev_string)

for i in input_string:
    str.insert(0,i)

reverse_string = "".join(str)

print('Input String = ', input_string )
print('Reverse String = ',reverse_string, type(input_string) )


# return first non repeated lettter of string

input_string = input('Enter String value = ')

for i in input_string:
    if input_string.count(i) == 1:
        print('Char is = ', i)
        break

#factorial using while loop

input_val = int(input('Enter the factorial number = '))
factorial = 1

while (input_val > 0):
    factorial = factorial * (input_val) 
    input_val -= 1

print('factorial output = ', factorial)


# valid Input Checker

# input_value = int(input("Enter The number = "))

# if (input_value < 10 and input_value > 0):
#     print('Valid Input Value Thank You !')
# else:
#     while (input_value > 0):
#         print('Invalid Input Value Try Again !')
#         input_value = int(input("Enter The number = "))

#         if (input_value < 10 and input_value > 0):
#             print('Valid Input Value Thank You !')
#             break


while True:
    input_value = int(input("Enter The Right Input Value Between 1 to 10 = "))
    if (input_value < 10 and input_value > 0):
        print('Valid Input Value Thank You !')
        break
    else:
        print('Invalid Input Value Try Again !')



# prime number checker

prime_checker_value = int(input("Enter Value = "))
is_prime = True

if (prime_checker_value > 1):
    for i in range(2,prime_checker_value):
        if ((prime_checker_value % i) == 0):
            is_prime = False
            # print('Input Value is Not Prime Number !!')
            break
        else:
            # print('Input Value is Prime Number !!')
            is_prime = True
            break

print('Input value is Prime', is_prime)


# exponential backoff that double wait time on wrong input 
# use case in password reset , otp

import time

attempts = 0
waiting_time = 1
retry_limit = 5

while (attempts < retry_limit):
    print('Attempts = ',attempts + 1,' Waiting Time = ',waiting_time)
    time.sleep(waiting_time)
    attempts += 1
    waiting_time *= 2
    


# python behind the scenes structure of Loops Working model





