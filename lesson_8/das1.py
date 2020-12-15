deposit = 5000
percent = 0.09
yearManey = 0
incomeManey = 0

firstYearManey = deposit + deposit * percent
print('First year amount will be: ' + str(firstYearManey))

secondYearManey = firstYearManey + firstYearManey * percent
print('Second year amount will be: ' + str(secondYearManey))

thirdYearManey = secondYearManey + secondYearManey * percent
print('Third year amount will be: ' + str(thirdYearManey))




firstValue = int(input('Please input a first value\n'))
secondValue = int(input('Please input a second value\n'))
thirdValue =  int(input('Please input a third value\n'))

print(int(firstValue) + int(secondValue))
print(int(firstValue) - int(secondValue))
