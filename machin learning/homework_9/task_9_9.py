# Create a class circle for representing with some attributes (radius, center coordinates, PI number) and behavior,
# create instances and use them

# Создайте круг класса для представления с некоторыми атрибутами (радиус, координаты центра, число PI) и поведением,
# создавайте экземпляры и используйте их

import math


class Circle:
    def __init__(self, radius, center_coordinates):
        self.radius = radius
        self.center_coordinates = center_coordinates

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


r = int(input("Enter radius of circle: "))
obj = Circle(r, (5, 3))
print("Area of circle:", round(obj.area(), 2))
print("Perimeter of circle:", round(obj.perimeter(), 2))
