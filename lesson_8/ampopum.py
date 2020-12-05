# # stextsel tveri colection tpel ayn tveri gumarn voronq bazhanvum en 3-i
# """
# numbers = [10, 20, 3, 9, 18, 25, 33]
# sum = 0
# for num in numbers:
#     if num in numbers:
#         sum += num
#
# print(sum)
#
# ################comperetion#####
# import functools
#
# numbers1 = [num for num in numbers if num % 3 == 0]
# result = functools.reduce(lambda a, b: a + b, numbers1)
# print(result)
#
# ##################### filter ##############
#
# numbers1 = list(filter(lambda num: num % 3 == 0, numbers))
#
# ################
#
# # haytararel usanoxneri anunneri collection ptel kent indexsov annunnern ev verjinn
#
# student_name = ["Arina", "Hrayr", "Tatev", "Sevak", "Robert"]
# print(student_name[1::2], student_name[-1])
#
# ################### version 2
#
# for index in range(0, len(student_name)):
#     if index % 2 == 1:
#         print(student_name[index])
#
# ##############
# # haytararel meqenaneri colection, mutqagrel anunn stugel ka mer collectioni
# # mej te che ete ka tpel indexs
#
# car_names = ["BMW", "Audi", "Opel"]
# name = input("input name\n")
# if name in car_names:
#     print(car_names.index(name))
#
# ########### version 2 ###########
#
# for index in range(0, len(car_names)):
#     if car_names[index] == name:
#         print(index)
#
# ############################
# """
# # stextsel  guneri 2 colection tpel bolorguynern aranc krknutyunneri
# # tpel ayn guynern voronq kan arajinum ev chkan erkrordum
#
# color_list_1 = {"red", "blue", "yellow", "black"}
# color_list_2 = {"dark_red", "blue", "yellow", "borrow", "orange"}
# new_color_list = color_list_1 | color_list_2
#
# print("miavorum", new_color_list)
# print("hanum", color_list_1 - color_list_2)
# print(color_list_1 & color_list_2)
#
# ########################
# mutqagrel text hashvel qani hat "ab" ka nshvats teqsti mej  stugel zuyg e te voch qanakn "ab"

# str1 = input("input string\n")
# count = str1.count("ab")
# if count % 2 == 0:
#     print("zuyg e")
# else:
#     print("kent e")

# print(dir(str))
# print(help(str.count))

####################################
# sarqel tveri collection tpel skzbic minchev kesn
#
# num_list = [10, 25, 33, 44, 55, 254, 458]
# print(num_list[:len(num_list) // 2])

###############
# strxtsel usanoxneri ev irenc bazhinneri
# collection tpel qani hat bajin ka, qni usanox ka,
# tpel vor bazhnum e mutqagrvats uzanoxn
# qani bazhni anun e sksum "s" ov avelacnel usanox ira bazhnov

students = {"Arina": "tntes", "Hrayr": "Tht", "Sevak": "Mat", "Levon": "Tht"}
unical_bajin = set(students.values())
print("unical bajinner", len(unical_bajin))
print("usanoxneri qanak", len(students))
new_list2 = list(filter(lambda name: name[0] == "S", students))
print("sksvuma s ov", new_list2)
students[input("stud name: ")] = [input("student kurs: ")]
name = input("mutqagrel anunn stugelu hamar bajinn: ")
if name in students.keys():
    print(students[name])
