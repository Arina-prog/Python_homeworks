# Create a class for representing a ticket with some attributes (from location, to location, transport type,
# duration in minutes, arrival time, passenger) and behavior (set from/to, change transport type, increase
# duration by some number, set passenger), create several tickets and perform operations on them

# Создайте класс для представления билета с некоторыми атрибутами (из местоположения в местоположение,
# тип транспорта, продолжительность в минутах, время прибытия, пассажир) и поведением (установить из / в,
# изменить тип транспорта,
# увеличить продолжительность на некоторое число, установить пассажира) , создайте несколько тикетов и выполните над
# ними операции
class Ticket:
    def __init__(self, from_location, to_location, transport_type, duration_minutes, arrival_time, passager):
        self.from_location = from_location
        self.to_location = to_location
        self.transport_type = transport_type
        self.duration_minutes = duration_minutes
        self.arrival_time = arrival_time
        self.passager = passager

    def set_location(self, fromm, to):
        self.from_location = fromm
        self.to_location = to

    def change_transport_type(self, t_type):
        self.transport_type = t_type

    def increase_duration(self, minuts):
        self.duration_minutes += minuts

    def passagers(self, name):
        self.passager = name

    def show(self):
        print("from location - " + self.from_location, "\n",
              "to location - " + self.to_location, "\n",
              "transport type -  " + self.transport_type, "\n", "duration minutes - " + str(self.duration_minutes),
              "\n",
              "arrival time - " + str(self.arrival_time), "\n", "passager - " + self.passager, "\n")


ertuxi_1 = Ticket("Erevan", "Sisian", "mikroavtobus", 180, {17: 00}, "Ani Balyan")
ertuxi_1.show()
print("__________passager 1_________")

passager_1 = Ticket("Erevan", "Sevan", "mikroavtobus", 120, {14: 15}, "A.saiyan")
passager_1.show()
print("__________from/to_________")

passager_1.set_location("Gyumri", "Ijevan")
passager_1.show()

print("__________change transport type_________")

passager_1.change_transport_type("Audi")
passager_1.show()

print("__________increase_duration_________")

passager_1.increase_duration(52)
passager_1.show()

print("__________add passager_________")

passager_1.passagers("Arman")
passager_1.show()

passager_2 = Ticket("Armavir", "Ejmiatsin", "avtobus", 65, {18: 00}, "G.Mheryan")
passager_2.show()

passager_2.set_location("Gyumri", "Vanadzor")
passager_2.show()

print("__________change transport type_________")

passager_2.change_transport_type("Opel")
passager_2.show()

print("__________increase_duration_________")

passager_2.increase_duration(65)
passager_2.show()

print("__________add passager_________")

passager_2.passagers("Artak")
passager_2.show()
