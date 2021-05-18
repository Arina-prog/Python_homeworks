# Create a class for representing animal, create a class for bear and class for wolf, create objects and use them

# Создайте класс для представления животных, создайте класс для медведя и класс для волка, создавайте
# объекты и используйте их

class Animal:
    def __init__(self, name, color, leg=4):
        self.name = name
        self.color = color
        self.leg = leg

    def speed_run(self):
        print("80")


class Bear(Animal):

    def voice(self):
        print("brrrr")

    def speed_run(self):
        print("50km/h")


class Wolf(Animal):

    def yell(self):
        print("auuuu")

    def speed_run(self):
        print("60km/h")


print("______bear______")
bear = Bear("Max", "borrow")
print(bear.color)
print(bear.name)
print(bear.leg)
bear.voice()
bear.speed_run()
print("______wolf______")

wolf = Wolf("Jeck", "whate", 3)
print(wolf.color)
print(wolf.name)
print(wolf.leg)
wolf.yell()
wolf.speed_run()
