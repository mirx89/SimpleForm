from math import pi


class Circle:

    def __init__(self, radius):
        """ Loo klass koos raadiusega """
        # print("Object created")
        self.radius = radius

    def get_radius(self): # tegelikust poleks vaja olnud. Pääseme ligi ilma funktsioonite
        # print("Return radius")
        return self.radius

    def diameter(self):
        return 2 * self.radius

    def area(self):
        #pi * pwo(self.radius, 2) # import pow
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius