# Create a collection for storing hotel visitors (name, country), input several visitors from console,
# print how many visitors are now in hotel, what is their country, what is their name
# Создайте коллекцию для хранения посетителей отеля (название, страна), введите несколько посетителей с консоли,
# распечатайте, сколько посетителей сейчас в отеле, какая их страна, как их зовут

hotel = {"Ani": "Armenian", "Gary": "Russian", "Jek": "UK"}
# hotel = {}
count = 0
number = int(input("number visitors:\n"))
while(count < number):
    hotel[input("name:\n ")] = input("country:\n ")
    count += 1
    print(len(hotel))
print(hotel)

