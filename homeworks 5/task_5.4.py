# Input a string, print it from start to half if its length is even,
# otherwise from half to the end
# 4..Введите строку, распечатайте ее от начала до половины,
# если ее длина четная, в противном случае от половины до конца

# str1 = "helow+world"
str_1 =input('input str\n')
length = len(str_1)
print(length)
if length % 2 == 0:
    c = int(length/2)
    print(c)
    print(str_1[0:c])
else:
    c = int(length/2)
    print(str_1[c:length])

print(str_1[1::2]) if (len(str_1)%2 == 0) else print(str_1[::2])
