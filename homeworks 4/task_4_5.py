# Define a garage collection that stores 3 cars (models),
# it’s known that double of same models came to garage, print garage models
# 5..Определите гаражную коллекцию, в которой хранятся 3 машины (модели),
# # известно, что в гараж пришли две одинаковые модели, распечатайте модели гаража

garage = ["mersedes", "opel", "bmw"]
car_models1 = input("input car model 1:\n")
car_models2 = input("input another car model:\n")
some_car_mod = []
for car in garage:
    if car == car_models1 or car == car_models2:
        some_car_mod.append(car)
if len(some_car_mod) > 0: print(some_car_mod, ' are already in our garage')
print('there isn\'t same models in garage')
