
'''
inheritance 

it is process of inheriting parent class function and parameter into child class

'''

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        print('Circle Radius = ',self.radius)

    def circle_info(self):
        print('Radius =',self.radius)
        area = round(math.pi * self.radius * self.radius,2)
        circf = round(2 * math.pi * self.radius,2)
        print(f'Area = {area}, Circumference = {circf} for Circle Radius = {self.radius}')


class CircleData(Circle):
    def __init__(self,radius):
        # 2 types to call parent class init() method 1] super() , parent_class name()
        #  Circle.__init__(self,radius)
        super().__init__(radius) # recommended practice 
       
    def find_area(self):
        area = round(math.pi * self.radius * self.radius,2)
        return area

    def find_circumference(self):
        cirf =  round(2 * math.pi * self.radius,2)
        return cirf
    

# Note: Use the pass keyword when you do not want to add any other properties or methods to the class.

class CircleInfo(Circle):
    pass


c1 = Circle(10)
c2 = CircleData(20)
c3 = CircleData(30)
c4 = CircleInfo(40)

# parent class cannot access child class method 
# print('Area =',c1.find_area(),' Circumference = ',c1.find_circumference() )


#but child class can access parent class method
c3.circle_info()
c4.circle_info()

print('Area =',c2.find_area(),' Circumference = ',c2.find_circumference(), 'Radius =', c2.radius )




