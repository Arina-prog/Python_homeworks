# *Create a collection of filenames with their size, print how many files are greater than 15Mb,
# how many filenames start from ‘a’ letter, increase size of the file which name ends with ‘.txt’
# Создайте коллекцию имен файлов с указанием их размера, распечатайте, сколько файлов превышает 15 МБ,
# сколько имен файлов начинается с буквы «a», увеличьте размер файла, имя которого заканчивается на «.txt»

file_name = {"text": 20, "homwork": 30, "acua": 40,  "lasson": 10, "canon.txt": 32, "auto": 14, "akba.txt": 42}
print(file_name)
count = 0
count_a = 0
for fail in file_name.values():
    if fail > 15:
        count += 1
print("files are greater 15mb: " + str(count))
for fail in file_name.keys():
    if fail[0] == "a":
        count_a += 1
print("filenames start from <a>: " + str(count_a))
lis1 = []
for fail in file_name.keys():
    if ".txt" in fail:
        file_name[fail] = 50
        lis1.append(fail)

print("increase size of the file which name ends with ‘.txt’" + str(lis1))
print(file_name)