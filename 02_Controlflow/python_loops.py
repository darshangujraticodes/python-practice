
'''
Python Loops
'''

# Problem Statement 1

input_val = int(input('Enter your number = '))

def sum_of_num(number):
    sum = 0
    while (number > 0):
        rem = int(number % 10)
        sum = sum + rem
        number = int(number / 10)   
    
    return sum

print('Sum of Input Number = ', sum_of_num(input_val))