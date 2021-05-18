# Create a class for representing shop with some attributes (employees names, products names and prices, income, owner)
# and behavior (add employee, remove employee, add products, find product by name, find products cheaper than some
# specific value, change owner, increase income),
# create several shops and perform operations on them
# * Создайте класс для представления магазина с некоторыми атрибутами (имена сотрудников, названия продуктов и цены,
# доход, владелец) и поведением (добавить сотрудника, удалить сотрудника, добавить продукты, найти продукт по имени,
# найти продукты дешевле, чем определенная стоимость, сменить владельца , увеличиваем доход),
# создаем несколько магазинов и проводим над ними операции

class Market:
    """This is market class"""
    employees_names = []
    products_names_prices = {}

    def __init__(self, employees_names, products_names_prices, income, owner):
        self.employees_names = employees_names
        self.products_names_prices = products_names_prices
        self.income = income
        self.owner = owner

    def add_employee(self, name):
        self.employees_names.append(name)

    def del_employee(self, name):
        if name in self.employees_names:
            self.employees_names.remove(name)

    def add_products(self, name, price):
        self.products_names_prices[name] = price

    def find_product(self, name):
        if name in self.products_names_prices.keys():
            print(name, self.products_names_prices[name])
        else:
            print("that producn is spend")

    def products_cheaper(self, price):
        filt = list(filter(lambda key: self.products_names_prices[key] < price, self.products_names_prices))
        print(filt)

    def increase_income(self, income):
        self.income += income

    def change_owner(self, name):
        self.owner = name

    def show(self):
        print("employees_names is " + str(self.employees_names), "\n",
              "products_names_prices is " + str(self.products_names_prices), "\n",
              "income  " + str(self.income), "\n", "owner " + str(self.owner), "\n")


meat = Market(employees_names=["Ani", "Areg", "Nshan", "Vard", "Karen"], products_names_prices={"banan": 250, "hac": 200,
                                                                                             "sok": 260}, income=42000,
              owner="Grigoryan")
meat.show()
print("*******add employee********")
meat.add_employee("Karapet")
meat.show()
print("*****del employee**********")
meat.del_employee("Ani")
meat.show()
print("********new owner*******")
meat.change_owner("A.Barsexyan")
meat.show()
print("********increase income *******")
meat.increase_income(42000)
meat.show()
print("********find product name *******")
meat.find_product("sok")
meat.show()
print("********add products *******")
meat.add_products("kokos", 450)
meat.add_products("hac", 200)
meat.show()
print("********products cheaper*******")
meat.products_cheaper(400)
meat.show()

print("_________market is_meat______")

meat = Market(employees_names=["Anita", "Aregnaz", "Nushik", "Vardges", "Karlen"], products_names_prices=
{"tavari_mis": 2500, "xozi_mis": 2200, "vochxari_mis": 3000, "havi_mis":1000}, income=32600, owner="T.Mkrtchyan")
meat.show()
print("*******add employee********")
meat.add_employee("Gayane")
meat.show()
print("*****del employee**********")
meat.del_employee("Anita")
meat.show()
print("********new owner*******")
meat.change_owner("D.Manukyan")
meat.show()
print("********increase income *******")
meat.increase_income(42000)
meat.show()
print("********find product name *******")
meat.find_product("xozi_mis")
meat.show()
print("********add products *******")
meat.add_products("dzuk", 1250)
meat.add_products("napastak", 2000)
meat.show()
print("********products cheaper*******")
meat.products_cheaper(3000)
meat.show()