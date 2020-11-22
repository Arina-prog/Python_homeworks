# Create a collection of hotel rooms (room number, state (booked or not),
# type (econom, business, lux)), calculate how many rooms are booked (create a function),
# calculate how many numbers of different types by default lux number
# s are free (create a function), generate a collection of econom numbers, print results
#Создайте коллекцию гостиничных номеров (номер комнаты, состояние (забронировано или нет),
# тип (эконом, бизнес, люкс)), посчитайте, сколько номеров забронировано (создайте функцию),
# посчитайте, сколько номеров разных типов (по умолчанию номера люкс) свободны (создать функцию),
# сгенерировать коллекцию эконом номеров, распечатать результаты

hotel = {125:["booked","econom"], 264:["free", "business"],
24:["free", "lux"], 25:["free","econom"],
64:["free", "business"], 124:["free", "lux"],325:["booked","econom"], 101:["free", "lux"]}

def booked(glossary):
    count = 0
    for i in glossary.values():
        if  "booked" in i:
            count += 1
    return count

# print(booked(hotel))

def type_count(dic):
    free_ec = 0
    free_lux = 0
    free_bus = 0
    for i in dic.values():
        if i[1]== "econom" and i[0]=="free":
            free_ec  += 1
        if i[1] =="lux" and i[0] =="free":
            free_lux +=1
        if i[1] =="business"  and i[0] =="free" :
            free_bus += 1
    return  free_bus,free_ec, free_lux,

# print(type_count(hotel))

def econom(ec_num):
    count = []
    for itm in ec_num.items():
        if  itm [1][1] =="econom":
            count.append(itm)
    return count

print(econom(hotel))