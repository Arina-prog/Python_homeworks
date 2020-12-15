# Create a class for representing building with some attributes and behavior, create a classes for
# representing hotel building with specific attributes and behavior, create objects and use them

# Создайте класс для представления здания с некоторыми атрибутами и поведением, создайте классы для представления
# здания отеля с определенными атрибутами и поведением, создайте объекты и используйте их

class Building:
    """This is Building class"""

    def __init__(self, harkeri_qanak, senyakneri_qanak, amrutyan_gortsakic):
        self.harkeri_qanak = harkeri_qanak
        self.senyakneri_qanak = senyakneri_qanak
        self.amrutyan_gortsakic = amrutyan_gortsakic


class Hotel(Building):
    room_price = []
    room_status = []

    def __init__(self, harkeri_qanak, senyakneri_qanak, amrutyan_gortsakic, name, stars_count, room_price,
                 azat_senyakneri_qanak):
        Building.__init__(self, harkeri_qanak, senyakneri_qanak, amrutyan_gortsakic)
        self.name = name
        self.stars_count = stars_count
        self.room_price = room_price
        # self.room_status = room_status
        self.azat_senyakneri_qanak = azat_senyakneri_qanak

    def nor_aycelu(self, number):
        self.azat_senyakneri_qanak -= number

    def room_status(self):
        self.room_status = self.senyakneri_qanak - self.azat_senyakneri_qanak
        print(" zbaxvats e", self.room_status)

    def printed(self):
        print("hotel name " + self.name, "\n", "hotel stars " + str(self.stars_count), "\n",
              "harkeri qanakn " + str(self.harkeri_qanak), "\n",
              "senyakneri qanakn " + str(self.senyakneri_qanak), "\n",
              "amrutyan gortsakic " + str(self.amrutyan_gortsakic),
              "\n", "senyakneri arzheqn " + str(self.room_price), "\n",
              "azat senyakneri qanak " + str(self.azat_senyakneri_qanak), "\n", )


hottel1 = Hotel(harkeri_qanak=5, senyakneri_qanak=50, amrutyan_gortsakic=10, name="Dayana", stars_count=5,
                room_price=[10000, 12000, 14000, 18000, 20000],
                azat_senyakneri_qanak=32)

hottel1.printed()
hottel1.nor_aycelu(3)
hottel1.printed()
hottel1.room_status()
