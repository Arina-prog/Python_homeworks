 # inkapsulacia
# modelavorman gaxabar
# tvyalneri ev metodneri havaqacu e
# methode funkcia e vore patkanum e konkret obyekti
# obyekte uni bazmativ hatkutyunner, abstractione ayn e vor  anjatum e karevore)
# encapsulation - detalnere taqcnum e ayl clasneric .......liqe kud eka grac, avel info chtal ayl obyectnerin
#
# class Person:
#     """"this is class for Person"""
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year
#         self.sex = 'Male'
#     def printing(self):
#         print('this is name:', self.name)
#         print('this is year:', self.year)
#         print('this is sex:', self.sex)
#     def greet(self, last_name):
#         print('good afternoon', last_name)
#
# john = Person(name = 'john', year = 1996)
# john.printing()
# john.greet('Berberyan')
#
#
# class House:
#     """"this is house class"""
#     number = 0
#     created_houses = []
#     def __init__(self, number, floors, signalisation, is_open):
#         self.number = number
#         self.floors = floors
#         self.__signalisation = signalisation
#         self.__is_open = is_open
#         House.number += 1
#         House.created_houses.append(self)
#     def change_number(self, new_number):
#         self.number = new_number
#     def increment_floors(self):
#         self.floors += 1
#     def decrement_floors(self):
#         self.floors -= 1
#     def close(self):
#         self.__is_open = False
#         self.__turn_on()
#     def open(self):
#         self.__is_open = True
#         self.__turn_off()
#     def __turn_on(self):
#         if not(self.__signalisation):
#             self.__signalisation = True
#     def __turn_off(self):
#         if self.__signalisation:
#             self.__signalisation = False
#     def check_is_open(self):
#         if self.__is_open:
#             print('the house is Open')
#         else:
#             print('the house is Close')
#     def print_house_number():
#         print('this is number of created Houses:', House.number)
#
# first_house = House(17, 2, False, False)
# second_house = House(25, 1, True, True)
# print('Number of created Houses', House.number)
# print('Names of created Houses', House.created_houses)
# House.print_house_number()
#
# first_house.increment_floors()
# print(first_house.floors)
# first_house.decrement_floors()
# print(first_house.floors)
# first_house.check_is_open()
# second_house.check_is_open()