# Input collection of numbers, find last number which square root is less than 26, print it
# Введите набор чисел, найдите последнее число, квадратный корень которого меньше 26, распечатайте его

# number = [256, 246, 36, 24, 64, 81, 230]
number = []
calc = 1
count = int(input("input count of namb: \n"))
while(calc <= count):
    number.append(int(input("input number")))
    calc += 1
for num in number:
    if int(pow(num, 2)) < 26:
        result = num
print(num)
print(number)