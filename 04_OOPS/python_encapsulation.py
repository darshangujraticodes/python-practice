'''
python ecapsulation 

encapsulation it is a process to restrict the direct access to some components of an object
few methods or variable are been restricted from direct use by object

in python to encapsulate variable add double underscore to variable " __ " eg. self.__brand 
Double undersco define the privatization it restrict the use of variable by object

But there should be the way to get private variable data and it is by getter and setter methods
getter() methods will help you to fetch private variable data 

getter methods declare convention are 

def get_car_info():


'''


# here we will 
class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        # Double underscoe (__) denote the privatization of variable to restrict value access by object to perform encapsulation
        self.__price = price 

    # getter method is used to fetch private variable data 
    def get_car_price_info(self):
        return self.__price
    
    #setter method is used to update the private variable data
    def set_new_car_price(self, price):
        self.__price = price

    def car_info(self):
        info = f'Car Brand : {self.brand} Model : {self.model}'
        return info
    
    
car1 = Car('Tata','Nexon','10 lakh')


print(f'Car Brand : {car1.brand}, Model : {car1.model}')


# this will give error of no attribute
# print(f'Car Price = {car1.__price}')

# so lets fetch private variable data using getter method
print(f'Encapsulate Price value fetch through getter() = {car1.get_car_price_info()}')

# setter mthod call 
car1.set_new_car_price('14 lakh')
print(f'Encapsulate Price value update through setter() = {car1.get_car_price_info()}')







