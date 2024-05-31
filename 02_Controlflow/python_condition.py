#python condition statment

#problem 1 :   child (1-12) , Teenage (13-19) , Adult (20-59) and Senior (60+)


# note when get value in user input the data is in datatype of string so we need to convert into integrer to perform maths operation

person_age_str = input('Enter Person Age = ')

print(person_age_str, type(person_age_str))

person_age = int(input('Enter Person Age = '))

if (person_age <= 12):
    print("He/ She is in Child Category")

elif (person_age >= 13 and person_age <= 19 ):
    print("He/ She is in Teenage Category")

elif (person_age >= 20 and person_age <= 59):
    print("He/ She is in Adult Category")
    
else:
    print("He/ She is in Senior Category")
    


# problem 2 : movie ticket adult = $12 child = $8 and on wednesday $2 discount

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

'''
problem 3 : student grade system  A (90-100), B (80-89),
 C (70,79), D (60-69), F (below 60)
'''

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


# coffee order problem

# coffee_order_size = input('Enter Coffee order Size = ')

# coffee_extra_shot = input("Do you want Extra Shot y or n = ").lower()


if (coffee_extra_shot == 'y'):
    coffee_order = coffee_order_size + " Coffee with Extra Shot"
    print(coffee_order)

else:
    coffee_order = coffee_order_size 
    print(coffee_order)







