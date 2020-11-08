# Input string, find how many ‘ab’-s are inside
# * Введите строку, найдите, сколько ‘ab’ внутри

str1 = input("input word:\n")
count = 0
index = 0
for i in str1:
    if (index != len(str1) and str1[index]=="a" and str1[index+1] =="b"):
            count += 1
    index+=1
print(len(str1))
print(count)