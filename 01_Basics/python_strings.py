

"""
curiosity question

find the difference between this strings

repr('chai')

str('chai')

print('chai')   

"""


string_val = 'lemon tea'

print(string_val)

print(string_val[2])

print(string_val[0:5])

string_val2 = '01234567898'

print(string_val2[2:])

print(string_val2[:6])

print(string_val2[1:8:2])

print(string_val2[-1])

#string methods

string_val3 = "   Darshan                   is combination of         Frontend Developer and Backend Developer          "

print(string_val3.lower())

print(string_val3.upper())

# note python string is case sensitive 
print(string_val3.count('Developer')) # output will be 4

print(string_val3.count('developer')) # ouput will be zero 

print(string_val3.replace('Darshan','Rohit'))

# remve unwanted space in string specifiacly we we fetch data from customer input form

print(string_val3.strip())








