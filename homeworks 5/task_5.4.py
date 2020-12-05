# Input a string, print it from start to half if its length is even,
# otherwise from half to the end
# 4..Введите строку, распечатайте ее от начала до половины,
# если ее длина четная, в противном случае от половины до конца

str_3 =input('input str3\n')
c = len(str_3)
k=str_3.split(str_3[(c//2)])
print(k[0]) if (len(str_3 )% 2 == 0) else print (k[1])

###########version 1#############
str1 = "helow+world"
str_1 =input('input str\n')
length = len(str_1)
print(length)
if length % 2 == 0:
    c = int(length/2)
    print(c)
    # print(str_1[0:c])
    print(str_1[:c])
else:
    c = int(length/2)
    print(str_1[c:length])

###########version 2###############

str_2 =input('input str2\n')
k = len(str_2)
print(str_2[:(k//2)]) if (k % 2 == 0) else print(str_2[(k//2):])






