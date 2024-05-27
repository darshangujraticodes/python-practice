
# python numbers
# python is great with number and competitor for matplotlib

#arithmatic opr (+, -, /, *)


x = 2
y = 3
z = 4

print("add =",x+y,"quotient =", z/x, "Remainder =",x%y," power =", x**y )


#comparison opr ( >, < , == , != )

t1 = x < y < z 
print(x < y < z  )

t2 = x < y & y < z
print(x < y & y < z  )

#always avoid this case it will be rejected in code review operator precendence it unclear message

# while compairing number always note data type should be same float should not be compare with number

print(40 + 2.23) #wrong practice instead do 

print(float(40) + 2.23)

# operator overloading 

print("darshan"+" full stack developer")

# boolean comparison note boolean first letter is capital True, False

print(False == 0)

print( True == 1)


"""

""" """ Multi-line comment 
#single line comment

python note 3 types brackets
() => parenthysis   used for tuples
[] => sqaure bracket  used for list and array
{} -> curly braces  used for dictionary

"""

#import math library


import math
p = 3.14
q = -5.544
#move towards nearest smaller value
print("floor() = ",math.floor(p), math.floor(q) )  


p = 3.14
q = -5.544
#move towards nearest greater value
print("ceil() = ",math.ceil(p), math.ceil(q) )  

p1 = 3.14
q1 = -5.544
#move towards 0 of graph
print("trunc() = ",math.trunc(p1), math.trunc(q1))  


print("math square root = ",math.isqrt(64),"circle pi = ",math.pi )

# complex number

print((2+3j) * 5)


# decimal, hexadecimal, octal, binary

"""

declaration 

0o64     => 0o denote octal
0b1000   => 0b denote binary
0xFF   => 0x denote hexadecimal

but python have predefine methods

oct()
hex()
bin()
dec()


int('0o64 ',8)


"""

print("binary = ",bin(15)) 

print("octal = ",int('0o64',8))

print("binary = ",int('1110',2))




# import random library 

import random

print("random value generator = ",random.random())

#logic to genrate random value in integer +1 to not get 0 value in random
intval = int(random.random() * 10 + 1)

print("random integer value = ",intval)


#random integer bulit in function random.randint(1,6)
print("random integer = ", random.randint(1,6) )


#randomly select the value from given array
print("random choice =", random.choice([21,22,24,25,26,23]) )


#random shuffle is method which shuffle the array elements useful in shuffling card
arr = [2,4,8,15,7,9,8,74]
random.shuffle(arr)
print(arr)


# octal, binary, hexadecimal


#booleans 

#sets


