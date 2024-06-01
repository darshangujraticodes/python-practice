#python condition statment

#problem 1 :   child (1-12) , Teenage (13-19) , Adult (20-59) and Senior (60+)


# note when get value in user input the data is in datatype of string so we need to convert into integrer to perform maths operation

# person_age_str = input('Enter Person Age = ')

# print(person_age_str, type(person_age_str))

print('\n Person age Condition Problem 1')

person_age = int(input('Enter Person Age = '))

if (person_age <= 12):
    print("He/ She is in Child Category")

elif (person_age >= 13 and person_age <= 19 ):
    print("He/ She is in Teenage Category")

elif (person_age >= 20 and person_age <= 59):
    print("He/ She is in Adult Category")
    
else:
    print("He/ She is in Senior Category")

    
# ------------------------------

# problem 2 : movie ticket adult = $12 child = $8 and on wednesday $2 discount

print('\n Movie ticket Booking Problem 2')

age = int(input('Enter your Age = '))

day = input('Enter Booking Day = ').lower()

adult_ticket_price = 12

child_ticket_price = 8

if (day == 'wednesday'):
    if (age < 18):
        print('Your Ticket Price is $',child_ticket_price - 2)
    else:
        print('Your Ticket Price is $',adult_ticket_price - 2)

else:
    if (age < 18):
        print('Your Ticket Price is $',child_ticket_price)
    else:
        print('Your Ticket Price is $',adult_ticket_price)


# ------------------------------


'''
problem 3 : student grade system  A (90-100), B (80-89),
 C (70,79), D (60-69), F (below 60)
'''

print('\n Student Marks Problem 3')

student_marks = int(input('Enter Your Marks = '))

if (student_marks < 0 or student_marks > 100):
    print('Marks Input Value is Invalid !')
    exit()

elif (student_marks >= 90 and student_marks <= 100 ):
    print('Student Grade is A')

elif (student_marks >= 80 and student_marks <= 89 ):
    print('Student Grade is B')

elif (student_marks >= 70 and student_marks <= 79 ):
    print('Student Grade is C')

elif (student_marks >= 60 and student_marks <= 69 ):
    print('Student Grade is D')

else:
    print('Student Grade is F')



# ------------------------------

# coffee order problem

print('\n Coffee Order Problem 4')

coffee_order_size = input('Enter Coffee order Size = ')

coffee_extra_shot = input("Do you want Extra Shot y or n = ").lower()

if (coffee_extra_shot == 'y'):
    coffee_order = coffee_order_size + " Coffee with Extra Shot"
    print(coffee_order)

else:
    coffee_order = coffee_order_size 
    print(coffee_order)


# ------------------------------


# password validtaion

print('\n Valid Password Checker Problem 5')

password = input('Enter Your password = ')

# char = 'Darshan$85'
# not convert boolean value in opposite form true -> false an vice versa
#any() method  return true  or false on condition satisfy


def password_check(password_input):
    special_symbols = ['@','#','$','*','!']
    val = True

    if (len(password_input) < 6 ):
        print('Minimum length limit of Password is 6 ! ')
        val = False
        exit()
    
    if (len(password_input) > 13 ):
        print('Maximum length limit of Password is 12 ! ')
        val = False
        exit()

    if not any(char.isdigit() for char in password_input  ):
        print('Password must have one Numeric Digit')
        val = False
        exit()

    if not any(char.isupper() for char in password_input):
        print('Password must have one Uppercase Value')
        val = False
        exit()
        
    if not any(char.islower() for char in password_input):
        print('Password must have one Lowercase Value')
        val = False
        exit()
                
    if not any(char in special_symbols for char in password_input):
        print('Password must have one Special Symbols @,#,$,* and !  ')
        val = False
        exit()

    if val:
        return print('Passoword is Valid.')
    
password_check(password)




