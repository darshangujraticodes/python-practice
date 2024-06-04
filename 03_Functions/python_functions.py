
'''

Types of Function in Python 

basic functions
Normal Function 
lambda function
args function
kwargs function (keyword argument function)

'''

# find circle areas and circumference

import math

def circle_data(radius):
    area = math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius
    return area , circumference


# destructure return function returns

input_radius = int(input('Enter the Radius of Circle = '))

circle_area , circle_circumference = circle_data(input_radius)

print('Area of Cirle =',round(circle_area,2),'Circumference of Circle = ',round(circle_circumference,2))