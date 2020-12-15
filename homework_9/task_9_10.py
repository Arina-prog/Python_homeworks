#Create class Person with attributes (name, height that should be more than 30, sex that should be male or female)
# and some behavior, control the values, create objects and use them

#Создайте класс Person с атрибутами (имя, рост, который должен быть больше 30, пол, который должен быть мужской или
# женский) и некоторым поведением, контролировать значения, создавать объекты и использовать их

class Person:
    def __init__(self, name, height, sex):
        self.name = name
        if height>30:
            self.height = height
        if sex=="male" or sex =="female":
            self.sex = sex

class Man(Person):
    def __init__(self, name, height,sex, proffession):
        Person.__init__(self, (name, height, sex))
        self.proffession = "doctor"

#
#
# print(Person.age, Person.sex, Person.proffession,)
#
t =Person("aaa", 40, "male")
("aaa", 40, "male", "djh")
# age = Person()
print(Man("gvfkf",40, "mail","jghl"))
