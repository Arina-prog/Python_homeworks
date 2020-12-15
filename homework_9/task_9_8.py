# Create a class for representing a smartphone with related attributes (private, public, protected) and behavior,
# create objects and use them
#
# Создайте класс для представления смартфона со связанными атрибутами (частный, общедоступный, защищенный) и
# поведением, создавайте объекты и используйте их

class Smartphone:
    """"this is smartphone class"""
    def __init__(self, type, color, signalisation, is_open):
        self.type = type
        self.color = color
        self.__signalisation = signalisation
        self.__is_open = is_open
