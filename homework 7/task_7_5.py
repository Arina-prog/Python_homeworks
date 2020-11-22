# Create a collection of company names, generate a collection of company names
# ending with ‘s’ (create a function), generate a collection of company names containing different
# symbols combination by default double ‘o’ (create a function), print results
#Создайте коллекцию названий компаний, сгенерируйте коллекцию названий компаний,
# оканчивающихся на «s» (создайте функцию), сгенерируйте коллекцию названий компаний,
# содержащих различные комбинации символов по умолчанию, двойной «o» (создайте функцию), распечатайте результаты

company_name= ["kit kat", "Coca colla", "Oracle", "UPS", "Mars", "Astromaps", "Google", "Moodle", "Joomag"]
comb = input("input simbol combination:\n ")
def search_s(arr):
    names= []
    for name in arr:
        if name[-1] == "s" or name[-1] == "S":
            names.append(name)
    return names

# print(search_s(company_name))

def search_oo(arr, simv):
    names= []
    for name in arr:
        if simv in name:
            names.append(name)
    return names

print(search_oo(company_name, comb))