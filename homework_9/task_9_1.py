# *Create a class for representing book with some attributes (author, owner, pages, price, current page)
# # and behavior (change owner, increase price, change current page), create several books and perform operations on them
# * Создайте класс для представления книги с некоторыми атрибутами (автор, владелец, страницы, цена, текущая страница) и
# поведением (сменить владельца, увеличить цену, изменить текущую страницу), создать несколько книг и выполнить с ними
# операции

class Book:
    """this is class of Book"""

    def __init__(self, author, ower, page, price, new_page):
        self.author = author
        self.ower = ower
        self.page = page
        self.price = price
        self.new_page = new_page

    def change_ower(self, ower):
        self.ower = ower

    def increase_price(self, price=125):
        self.price += price

    def current_page(self, page=25):
        if self.new_page + page < self.page:
            self.new_page += page
        else:
            self.new_page = "<<end book>>"
        return self.new_page

    def show(self):
        print("Book author is " + self.author, "\n", "Book ower is " + self.ower, "\n", "Book page " + str(self.page),
              "\n", "Book price " + str(self.price), "\n", "Book current page " + str(self.new_page), "\n")


# ##############class book t ########
t = Book("sheqspir", "Dianna", 468, 7500, 365)
t.show()
print("_______change ower___________")
t.change_ower("Narek")
t.show()
print("_________increase price_____________")
t.increase_price(600)
t.show()
print("________courrent_page__________")
t.current_page(350)
t.show()
print("/////////////////")

################ book1###########
book1 = Book("M.Gosh", "Anna", 865, 6980, 140)
book1.show()
print("_______change ower____book1_______")
book1.change_ower("Inga")
book1.show()
print("_________increase price_____book1________")
book1.increase_price(1200)
book1.show()
print("________courrent_page____book1______")
book1.current_page(126)
book1.show()
print("/////////////////")
################ book2###########
book2 = Book("A. Dyuma", "Nvard", 755, 10000, 36)
book2.show()
print("_______change ower____book2_______")
book2.change_ower("Lena")
book2.show()
print("_________increase price_____book2________")
book2.increase_price(500)
book2.show()
print("________courrent_page____book2______")
book2.current_page(110)
book2.show()
print("/////////////////")
