#*Calculate multiplication of numbers from 0 to inputed value and print it
# * Рассчитайте умножение чисел от 0 до входного значения и распечатайте его
mult = 1
count = 1
# count = 0
vaiue = int(input("input namber : \n"))
while(count <= vaiue):
    mult *= count
    count += 1
print("multiplacation is " + str(mult))
print('multiplacation is ', mult)
