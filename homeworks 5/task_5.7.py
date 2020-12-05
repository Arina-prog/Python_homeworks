# Input string, find how many ‘ab’-s are inside
# * Введите строку, найдите, сколько ‘ab’ внутри

str_2 = input('Input string 2\n: ')
number_of_ab = str_2.count('ab')
print(number_of_ab)

###################

str1 = input("input string 1:\n")
count = 0
index = 0
for i in str1:
    if (index != len(str1) and str1[index]=="a" and str1[index+1] =="b"):
            count += 1
    index+=1
print(len(str1))
print(count)


