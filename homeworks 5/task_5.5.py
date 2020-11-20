# Calculate number of ‘d’ chars in inputed string
# 5.. Вычислить количество символов «d» во введенной строке

# str1 = "ghsagdddanh"
str1 = input("input str\n")
count = 0
for char in str1:
    if char == "d":
        count += 1
print("count char d = " + str(count))
print("count char d = ",  str(count))
