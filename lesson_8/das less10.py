# class Animal:


# def __init__(self, name, sex, animal_type):
#         self.name = name
#         self.sex = sex
#         self.anymal_type = animal_type
#     def eat(self):
#         print(self.name, 'is eating')
#
# class Lion(Animal):
#     def __init__(self, name, sex, animal_type, hair_length):
#         Animal.__init__(self,name, sex, animal_type)
#         self.hair_length = hair_length
#     def hunt(self):
#         print(self.name, 'hunts zafras')
#     def eat(self):
#         super().eat()
#         print(self.name, 'is eating a meat')
#
# class Elephant(Animal):
#     def __init__(self, name, sex, animal_type, hobbot_length):
#         Animal.__init__(self, name, sex, animal_type)
#         self.hobbot_length = hobbot_length
#     def drink(self):
#         print(self.hobbot_length, 'this is length of elefant\s hobbot')
#
# lion = Lion('Lion', 'female', 'carnivore', 20)
# elephant = Elephant('Elephant', 'male', 'harbivore', 100)
# lion.eat()
# lion.hunt()
# elephant.drink()


# override noric grel
# super() ete uni parent class, karoxenq grel super().merUzacFunctian vercnel
# isinstance(obj, type) stugume classe veradacnum e bool
# getter and Setter \stacoxner ev poxoxner
#
# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#     @property
#     def day(self):
#         return self._day
#     @day.setter
#     def day(self, new_day):
#         if new_day >= 1 and new_day <= 15:
#             self._day = new_day
#
#     def print_day(self):
#         print(self.day)
#
#
# my_birthday = Date(14, 4, 1996)
# my_birthday.day = -2
# my_birthday.print_day()
# my_birthday.day = 10
# my_birthday.print_day()

def divide():
    try:
        print(int(input('first num: ')) // int(input('sec num: ')))
    except ZeroDivisionError:
        print('problem with dividing with Zero')
    except:
        print('some other problem')
    finally:
        print('the action is finish')


divide()
print('some text after divide')
