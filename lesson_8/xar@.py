# haytararel kahuyq klass vorosh atributnerov(anvanum, guyn gin) mi sharq gortsoxutyunnerov ( tpel anvanumn,
# poxel guyn@) haytararel sexan klass vorosh atributnerov (anvanum, guyn gin, materyalner irenc %-ov) mi sharq
# gortsoxutyunnerov ( tpel anvanumn, poxel gin@, tpel amenabardzr %-ov materyaln, arka e ardyoq materyal A"-ov sksvox,
# hashvel materyalneri qanakn) stextsel 2 sexan katarel gortsoxutyunner, tpel irenc hamar @ndhanur materyalneri
# anvanumnern

class Furniture:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self._price = new_price

    def print_name(self):
        return self.name

    def change_color(self, color):
        self.color = color


class Table(Furniture):
    def __init__(self, name, color, price, materyals):
        super().__init__(name, color, price)
        self.materyals = materyals

    def max_materyal(self):
        max_procent = 0
        name = ""
        for key in self.materyals.keys():
            if self.materyals[key] > max_procent:
                max_procent = self.materyals[key]
                name = key
        return name

    def materials_A(self):
        for key in self.materyals.keys():
            if key[0] == "A":
                print("yes ", key)

    def materials_count(self, ):
        print(len(self.materyals))


ator = Furniture("poqr_ator", "dexin", 1500)
ator.price = 2500
print(ator.price)
ator.price = -458
print(ator.price)
print(ator.name)
print(ator.color)

poqr_sexan = Table("klor_sexan", "sev", 4500, {"Payt": 20, "Laminat": 30, "Apaki": 5})
print(poqr_sexan.name)
print(poqr_sexan.price)
print(poqr_sexan.color)
print(poqr_sexan.materyals)
print("tpel amenamets %-ovn ", poqr_sexan.max_materyal())
print(poqr_sexan.materials_A())
print(poqr_sexan.materials_count())

mets_sexan = Table("uxankyun sexan", "darchnaguyn", 542000, {"Laminat": 40, "Payt": 10, "Nerk": 5})
set_1=set(mets_sexan.materyals.keys())
set_2 = set(poqr_sexan.materyals.keys())
print(set_1 & set_2)