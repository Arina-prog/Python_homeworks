# Calculate number of ‘d’ chars in inputed string
# 5.. Вычислить количество символов «d» во введенной строке

str_2 = input('Input string 2 \n: ')
number_of_d= str_2.count('d')
print(number_of_d)

###################

# str1 = "ghsagdddanh"
str1 = input("input str 1\n")
count = 0
for char in str1:
    if char == "d":
        count += 1
print("count char d = " + str(count))
print("count char d = ",  count)
print(str1.find("d"))


