'''

Python decorator are of multiple types

staticmethod()
static method are the special method which can be only accecible trhough class but not through object. Note it is not similar to private in this we are just restricting object access

It has great application in python framework

#note in static method we  do not pass self parameter to cut of object access to method


Declares a static method in the class.
It cannot have cls or self parameter.
The static method cannot access the class attributes or the instance attributes.
The static method can be called using ClassName.MethodName() and also using object.MethodName().
It can return an object of the class.


'''

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def car_general_info1(self):
        print(f'Car Brand = {self.brand}, Model = {self.model} ')

    @staticmethod
    def car_general_info2(info):
        test = f'Car is best means of Transport for Family Tour ! {info}'
        return test

    

car1 = Car('Hyundai','Creta')
car1.car_general_info1()
print(car1.car_general_info2('with 10 lakh Creta'))


# static methods access through class
print(Car.car_general_info2('with 12 lakh Creata'))


# ---------------------


class Student:
    name = 'Sahil' # class attribute
    
    def __init__(self):
        self.age = 20  # instance attribute

    @staticmethod
    def tostring():
        print('Student Success ')


#object call
s1 = Student()
print(s1.age, s1.name)

s1.tostring()
Student.tostring()
