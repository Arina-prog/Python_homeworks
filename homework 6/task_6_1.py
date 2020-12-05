#Create constant collection of numbers, print first size of the collection and elements on even positions
# Создавайте постоянный набор чисел, печатайте первый размер коллекции и элементы на четных позициях

#####tuple#####
numbers = (15, 24, 36, -56, 89, 24, -13, 88,)
print(len(numbers))
even_pos_num = numbers[::2]
print('even positions num:', even_pos_num)

##################################

numbers = [15, 24, 36, -56, 89, 24, -13, 88]
count = 0
even_num = []
for num in numbers:
    if num % 2 == 0:
        count += 1
        even_num.append(num)
print(even_num)
print(len(numbers))



