
# Python math operation 

import math

x = max(15,4,4546)
y = min(656,665,65)
z = abs(-454)
p = round(45.5458,2)

print(x,y,z)

print(f'{math.sqrt(64)}, {math.ceil(8.5)}, {math.floor(8.5)}, {round(math.pi,2)}')


# Python with JSON data handling 

import json

# note json data is taken in string format 
json_user_data = '{ "id": 1, "name": "Sahil Sharma", "username": "sahilsharma", "email": "sahil@gmail.com", "website": "sahilsharaminfo.com" }'

print('\nJson Data type', type(json_user_data))

# convert json data in python dictionary using json.loads()

python_user_data = json.loads(json_user_data)

print('\nUser Data = ',python_user_data,type(python_user_data), python_user_data['name'])

# convert python objects into json strings

python_car = {
    'brand':'Tata',
    'model':'Nexon',
    'price':'10 lakhs',
    'type': 'electric car',
    'seater': '5 seater'
}

json_car = json.dumps(python_car)

print('\nJSON Car Data =',json_car, type(json_car))


# Regular Expression

import re

#password validation using regex

# password_input = input('\nEnter your password : ')
password_input1 = "Rahul#1234"

password_pattern = r"^(?=.*\d)(?=.*[@$!%*#?&])(?=.*[a-z])(?=.*[A-Z]).{8,15}$"

#compile this hard pattern in machine language

pat = re.compile(password_pattern)

# re.fullmatch(regex_pattern, input_text) and re.search((regex_pattern, input_text) work in same manner

if re.fullmatch(password_pattern,password_input1):
    print('Password is Valid')

else:
    print('Password is Invalid')


# refer this article for regular expression info : https://www.w3schools.com/python/python_regex.asp
