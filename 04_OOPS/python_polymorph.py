
'''
polymorphism is german word created by joining 2 word 
poly => many morph => form   :  manyform

here vehicle_movement and vehicle_info are same name method in class but has different working parameter 
'''


class Transport:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price


class Car(Transport):
    def __init__(self,brand, model, price):
        super().__init__(brand, model, price)

    def vehicle_movement(self):
        return 'Car Movement is called "Driving !" '
    
    def vehicle_info(self):
        info = f'Vehicle Type: Car, Brand : {self.brand}, Model : {self.model}, Price : {self.price}'
        return info
    

class Plane(Transport):
    def __init__(self,brand, model, price):
        super().__init__(brand,model,price)

    def vehicle_movement(self):
        return 'Car Movement is called "Flying !" '

    def vehicle_info(self):
        info = f'Vehicle Type: Car, Brand : {self.brand}, Model : {self.model}, Price : {self.price}'
        return info    
    

class Ship(Transport):
    def __init__(self,brand, model, price):
        super().__init__(brand,model,price)

    def vehicle_movement(self):
        return 'Car Movement is called "Sailing !" '   

    def vehicle_info(self):
        info = f'Vehicle Type: Car, Brand : {self.brand}, Model : {self.model}, Price : {self.price}'
        return info
        

c1 = Car('BMW','M4 Competition','1.2 Crore')
print('\n',c1.vehicle_info())
print(c1.vehicle_movement())



a1 = Plane('Boeing','Unified 737 MAX', '800 Crore')
print('\n',a1.vehicle_info())
print(a1.vehicle_movement())



s1 = Ship('Yacht','MAJESTY 160','2 Crore')
print('\n',s1.vehicle_info())
print(s1.vehicle_movement())



