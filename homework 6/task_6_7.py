#*Calculate multiplication of numbers from 0 to inputed value and print it
# * Рассчитайте умножение чисел от 0 до входного значения и распечатайте его
mult = 1
count = 1
value = int(input("input namber : \n"))
while(count <= value):
    mult *= count
    count += 1
print("multiplacation is " + str(mult))
print('multiplacation is ', mult)
