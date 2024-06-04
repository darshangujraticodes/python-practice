
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

print('Enrolled User Name is ',enrol_user_data1)
print('Enrolled User Name is ',enrol_user_data2)



# Lambda Function 
'''
this is useful to create function which is used for temporary period of only one time


'''






