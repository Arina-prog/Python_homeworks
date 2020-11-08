#Define a collection of numbers, generate a new collection
# selecting only odd or dividable by 6 numbers and print it
# 12. sahmanel tveri havaqatsu, stextsel nor havaqatsu  @ntrelov miayn
# kent kam 6-i bazhanvox tvern ev tpel

lis1 = [1, 24, 65, 85, 478, 25, 654, 258, 369, 41, 13, 47]
lis2 = []
calc = 1
for num in lis1:
    if num % 6 == 0 or (calc != num/2 and num % calc != 0):
        calc += 1
        lis2.append(num)
print(lis2)
print(lis1)