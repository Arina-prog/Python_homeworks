#Define an empty collection, input 3 numbers and add them to collection, calculate factorial for the last one
# # 7..Определите пустую коллекцию, введите 3 числа и
# # добавьте их в коллекцию, вычислите факториал для последнего
#
num_list = []
while (len(num_list)!=3):
    num_list.append(input("input number\n:"))
print(num_list)
last_namber = int(num_list[2])
print(last_namber)
fact_step = 1
fact = 1
while (fact_step <= last_namber):
    fact = fact*fact_step
    fact_step += 1
print(fact)
