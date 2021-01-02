# Create a class for representing a smartphone with related attributes (private, public, protected) and behavior,
# create objects and use them

# Создайте класс для представления смартфона со связанными атрибутами (частный, общедоступный, защищенный) и
# поведением, создавайте объекты и используйте их

class Smartphone:
    """"this is smartphone class"""

    def __init__(self, types, color, coll_song, password, contacts):
        self.types = types
        self.color = color
        self._coll_song = coll_song
        self.__password = password
        self.__contacts = contacts

    def status_phone(self, password):
        if password == self.__password:
            print("lock is open")
        else:
            print("phone loched")

    def show(self):
        print("phone type is " + self.types, "\n", "phone color is " + self.color, "\n",
              "phone coll song is " + self._coll_song,
              "\n", "contacts " + str(self.__contacts), "\n", "password is " + str(self.__password))
    # def change_possword(self):


sony = Smartphone("Xperia_S1", "whate", "ding_dong", 123, {"Anna": 234568, "Narek": 1245862, "Aren": 25864})
sony.show()
print("____poxel zangn protected_____")

sony._coll_song = "tulu-lulu"
sony.show()

print("____poxel passwordn private_____")

sony._Smartphone__password = 245
sony.show()
sony.status_phone(245)
