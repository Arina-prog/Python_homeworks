numbers = []
count = int(input("numbers count\n"))
calc = 0
while(len(numbers)<count):
    numbers.append(int(input("input numbers\n")))
    calc += 1
print(numbers)