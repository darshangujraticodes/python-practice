
'''
polymorphism is german word created by joining 2 word 
poly => many morph => form   :  manyform


'''


import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def find_area(self):
        area = round(math.pi * self.radius * self.radius, 2)
        return area 
    


class CircleInfo(Circle):
    def __init__(self, radius):
        super().__init__(radius)

    def find_area(self):
        return super().find_area()
