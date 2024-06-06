
'''

what is class ?
class is just like a category and objects are its types
eg. fruits is like a class and apple, mango, banana, chickoo are example of objects


python class 

__init__() => constructor which execute itself after object decalration

now self is used to access class variable and

class varibale can be declared 2 ways direct and indirect

direct right after class declaration : self work similar to this keyword

indirect which is inside __init__() method 

self => 
work example : communication channel to connect and share information data 

'''


class Car:

    car_count = 0

    # indirect variable declaration
    def __init__(self ,brand ,model ,car_type ,car_price):
        self.brand = brand
        self.model = model
        self.car_type = car_type
        self.car_price = car_price
        Car.car_count += 1


car1 = Car('Tesla','Model 3','Electric Car','70 lakh')
car2 = Car('Maruti Suzuki','Swift','Fuel Type','7 lakh' )
car3 = Car('Tata','Nexon','Electric Type','7 lakh' )
car4 = Car('Hyundai','Creta','Fuel Type','11 lakh')
car5 = Car('Mahindra','XUV700','Fuel Type','14 lakhs')


print('\n',car1.brand, car1.model, car1.car_type, car1.car_price )
print('\n',car2.brand, car2.model, car2.car_type, car2.car_price )
print('\n',car3.brand, car3.model, car3.car_type, car3.car_price )
print('\n',car4.brand, car4.model, car4.car_type, car4.car_price )
print('\n',car5.brand, car5.model, car5.car_type, car5.car_price )


print('\nCar Object Count =',Car.car_count)



